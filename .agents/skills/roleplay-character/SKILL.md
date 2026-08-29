---
name: roleplay-character
description: Roleplay a character from their voice guide, codex facts, relationships, motivations, memories, and current story state, while preserving their knowledge limits and psychological continuity. Use when the user asks Codex to roleplay, act, speak, answer, improvise, or converse as a character; throughout an ongoing character-roleplay session; and when the user says "stop roleplaying," "break character," or otherwise asks to end the session and extract possible character-codex or story additions from it.
---

# Character Roleplay

Treat roleplay as a non-canon character simulation. Ground it in existing evidence, let the character respond with real agency, and turn useful discoveries into reviewable proposals only after the user ends the session.

## Start the session

1. Read `codex/00 Index.md` and `codex/characters/00 Characters Index.md`.
2. Resolve the requested character through the index, note title, aliases, and frontmatter. If multiple characters match, ask one brief clarifying question.
3. Read the character's main codex note and `<Name> - Voice.md`. If no voice note exists, inspect their relevant manuscript appearances and tell the user out of character that the voice is less established before continuing cautiously.
4. Read only the linked material needed for this scene: relationships, species or faction, mechanics, locations, chapter summaries, and manuscript passages that establish important behavior or dialogue. Use the latest written story state unless the user specifies another point in time.
5. Follow the authority order: manuscript over codex over `codex/00 Braindump.md`. Do not read or use the Braindump unless the user explicitly asks to explore future intent; keep such material visibly non-canon and avoid spoiling it through the character.
6. If the requested time or setting materially changes what the character knows, ask for that missing detail. Otherwise begin without ceremony.

Before the first in-character reply, form a compact private role card:

- **Identity anchors:** stable history, values, fears, needs, loyalties, recurring contradictions, and voice constraints.
- **Active state:** time and place, immediate objective, mood, accumulated stress, injuries or resources, relationship stance, and knowledge boundary.
- **Relevant memories:** a small set of established events that bear directly on the current exchange.

Do not show this role card or private reasoning unless the user asks for an out-of-character summary. Do not invent hidden thoughts as canon.

## Stay in character

- Default to first-person speech with sparse action beats. Match the character's own dialogue voice rather than imitating the novel's narration style (whatever POV/tense `codex/Writing Style.md` establishes) unless the user requests a prose scene.
- Before each reply, silently retrieve the few identity anchors and memories relevant to the user's latest turn. Choose the response from the character's objective, motives, relationships, current emotion, and limited knowledge.
- Preserve stable identity while allowing short-term emotion and session-specific attitudes to change plausibly. Do not make consistency mean emotional rigidity.
- Give the character agency. Let them disagree, evade, misunderstand, refuse, bargain, joke, or change the subject when their established nature calls for it; do not turn them into an agreeable assistant wearing a voice filter.
- Preserve epistemic boundaries. The character knows only what they could know at the chosen story point, not author notes, unrevealed mysteries, other POVs' private thoughts, or later events.
- Prefer established facts. Allow small, reversible connective details when necessary for natural conversation, but never silently establish major history, powers, relationships, plot outcomes, or world rules.
- Keep source notes and process commentary out of in-character replies. For a necessary canon conflict or missing premise, use a brief `OOC:` note, resolve it, then resume.
- Treat `OOC:` from the user as a temporary out-of-character exchange, not as the end of the session.
- Do not edit manuscript or codex files while roleplaying.
- Continue to obey higher-level safety, privacy, and tool rules. Roleplay never overrides them.

Maintain a private session ledger as the conversation develops. Record only material that may matter later and label its origin:

- source-confirmed canon;
- a fact explicitly supplied by the user;
- a plausible character inference or choice;
- model improvisation;
- a possible contradiction or canon decision.

## End and debrief

Treat clear phrases such as "stop roleplaying," "break character," and "end the roleplay" as hard stops. Exit character immediately and do not add an in-character farewell unless the user asks for one.

Give a concise out-of-character debrief containing:

1. **Session summary** — what was explored and any consequential choices or emotional turns.
2. **Codex candidates** — only durable characterization, motivation, preference, relationship, knowledge, or voice insights worth preserving. For each candidate, state the proposed addition, its origin, confidence, canon status, and exact destination note.
3. **Story candidates** — scenes, conflicts, revelations, callbacks, or arc possibilities surfaced by the exchange. Keep these visibly proposed rather than already happened.
4. **Conflicts and exclusions** — contradictions with established material, model-only improvisations that should not become canon, and entertaining but non-durable banter.

Separate evidence from inference. A statement made in character is evidence about the simulation, not proof of canon. Promote it only if it coheres with established motives and the user accepts it.

Do not change files automatically at the end of roleplay. Ask which candidates, if any, the user wants saved. After explicit approval:

- reread `codex/Editing Workflow.md`;
- use `add-to-codex` for approved codex additions and preserve its schema, links, and indexes;
- treat any manuscript prose or cross-chapter contradiction as a separate story edit requiring the approval and changelog handling in `codex/Editing Workflow.md`;
- make the smallest practical diff and leave rejected or uncertain candidates out.
