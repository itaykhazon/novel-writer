---
name: sync-skills
description: Check the {{NOVEL_TITLE}} project's skill folders (.agents/skills for Codex, .claude/skills for Claude Code) for drift against each other, and against the Cowork account originals they were ported from. Use when the user asks to sync, reconcile, or check skills across tools, after editing a skill in one tool, or periodically as upkeep. Reports differences; does not silently overwrite anything.
---

# Sync Skills Across Codex, Claude Code, and Cowork

{{NOVEL_TITLE}}'s writing/review skills exist in **three places** that don't update each
other automatically:

1. **`.agents/skills/`** in the vault — the canonical local copy. Codex CLI
   reads this directory natively (the open [agentskills.io](https://agentskills.io)
   standard).
2. **`.claude/skills/`** in the vault — a duplicate for Claude Code CLI, which
   reads this directory name instead of `.agents/skills/`. This is a plain
   copy, not a live link, because these two directories may sit on a
   network-mounted or cross-platform folder where symlinks aren't reliable.
3. **The Cowork account skills** — the original skills (chapter workflow,
   review, and craft skills alike) installed in the user's Claude account. This is
   where `.agents/skills/` was originally exported *from*, and it's the
   richest version (it can use Cowork-specific automation — parallel
   reviewer subagents, the device bridge — that the local copies had to
   generalize away). It is **not reachable by a local script**: there's no
   API for a CLI tool to read a Cowork account skill directly. Reconciling
   against it is a manual step (see below).

Because there are three copies and only two of them are locally diffable,
this skill has two different jobs depending on what you're checking.

## Job 1 — reconcile `.agents/skills/` against `.claude/skills/` (fully automatic)

Run the bundled script from the vault root:

```bash
python3 .agents/skills/sync-skills/scripts/diff_skill_dirs.py \
    --a .agents/skills --b .claude/skills
```

It reports, per skill folder: present in one location but not the other, or
present in both with different file content (compared by hash, so any change
— even whitespace — is caught).

**Direction of truth: `.agents/skills/` wins.** It's the directory named after
the open standard both ecosystems are converging on, and it's the one this
project treats as canonical. When the script reports drift:

- If `.claude/skills/<name>/` is missing or stale relative to
  `.agents/skills/<name>/`, copy the `.agents/skills/<name>/` folder over it
  wholesale.
- If `.agents/skills/<name>/` is *missing* something `.claude/skills/<name>/*`
  has (i.e. someone edited the Claude Code copy directly instead of the
  canonical one), don't just discard it — show the user the diff and ask
  whether the edit should be promoted into `.agents/skills/` (then propagated
  back down to `.claude/skills/`) or discarded. Never silently pick a side.

After reconciling, re-run the script to confirm zero drift before reporting
back to the user.

## Job 2 — check either local copy against the Cowork account original (manual, human-in-the-loop)

This can't be automated end-to-end because the Cowork account skills only
exist inside the user's Claude account, not on this machine. The workflow:

1. Ask the user to open a Cowork session (or ask Claude, in an existing Cowork
   session, in the {{NOVEL_TITLE}} project) to re-export the skill in question as a
   `.skill` file — the same way it was originally delivered when this
   `.agents/skills/` tree was first created. Cowork skills are account-level
   and can drift over time (the author or Claude editing them, or Anthropic
   updating a bundled skill), so this copy may no longer match what's on
   disk here.
2. Have the user save that `.skill` file somewhere reachable by this tool and
   unzip it (it's a plain zip archive) to a scratch folder, e.g.
   `/tmp/cowork-export/<skill-name>/`.
3. Run the diff script in single-skill mode:

   ```bash
   python3 .agents/skills/sync-skills/scripts/diff_skill_dirs.py \
       --a .agents/skills/<skill-name> --b /tmp/cowork-export/<skill-name> --single
   ```

4. Any drift here is expected to include **more** than the local copy has —
   Cowork automation (subagent orchestration, device-bridge tool calls,
   Claude-only frontmatter fields like `compatibility:` as a structured map)
   was deliberately generalized out when these skills were ported, and that
   generalization is not a bug to "fix" by re-copying blindly. Read the diff
   and decide, per finding, whether it's:
   - **New durable knowledge** added to the Cowork version since the port
     (a new house rule, a new checklist item) — pull that into the local
     copy, adapting away any Cowork-only tool references the same way the
     original port did.
   - **Cowork-only automation** that has no local equivalent — leave it out
     of the local copy, same as before.
   - **A local-only fix** made directly to `.agents/skills/` that hasn't been
     told to Cowork yet — flag it to the user so they can ask Claude to fold
     it back into the account skill (this session can't write to a Cowork
     account skill directly either).

## When to run this

- Whenever the user asks to "sync skills," "check skills are in sync," or
  similar.
- After hand-editing any file under `.agents/skills/` or `.claude/skills/` in
  this vault — reconcile immediately (Job 1) rather than letting drift
  accumulate.
- Periodically (e.g. the user brings it up, or after a chapter-cycle run that
  seemed to reveal a new house rule worth codifying) — worth doing Job 2 on
  whichever skill just proved itself outdated.

## What NOT to do

- Don't overwrite `.claude/skills/` or `.agents/skills/` without showing the
  user the diff first, unless they've explicitly said "just make them match,
  `.agents/skills/` is always right" as a standing instruction.
- Don't treat the absence of a Cowork `.skill` export as "no drift" — it
  means Job 2 hasn't been checked, not that the copies agree. Say so
  explicitly rather than reporting a clean bill of health you didn't verify.
- Don't invent content for a skill that only exists in one location without
  the corresponding source material (e.g. don't guess at what a missing
  `.claude/skills/<name>/references/*.md` should say — copy it from
  `.agents/skills/`, don't reconstruct it from memory).
