# AI-Shaped Prose Pattern Catalog

Research snapshot: 2026-08-16. Model habits change. Use this catalog as a revision aid, not a static blacklist or a way to infer authorship.

## Contents

- A. Contrastive scaffolding
- B. Stock fiction phrases
- C. Vague pseudo-specificity
- D. Canned connectors and signposts
- E. Hedging and connective filler
- F. Template rhythm
- G. Explained subtext and synthetic profundity
- H. Lexical clusters
- I. Voice flattening
- J. Over-dramatic landings and false closure
- False-positive safeguards

## Evidence calibration

### Stronger evidence: corpus or structured studies

- [Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models](https://openreview.net/pdf/39260f6fd0d1508d77e23b72617da91a4cfc08ee.pdf) is an anonymous ICLR 2026 submission under review. It compares thousands of model-generated creative-writing outputs with human corpora and reports model-family "slop fingerprints." It identifies creative-writing patterns such as `voice barely above a whisper`, `heart hammered ... ribs`, `eyes never leaving`, and `flickered`, and measures some `It's not X, it's Y` constructions at 6.3 times the human rate. Treat the method as promising but provisional because the paper is not yet peer-reviewed and does not profile current Claude or ChatGPT directly.
- [People who frequently use ChatGPT for writing tasks are accurate detectors of AI-generated text](https://aclanthology.org/2025.acl-long.267/) reports that experienced LLM users relied most often on vocabulary (53.1% of explanations) and sentence structure (35.9%), including `not only ... but also`, `it's not just this, it's this`, consistent triples, low sentence-length variation, safe phrasing, and over-explanation. Detection still produces false positives.
- [Why Does ChatGPT "Delve" So Much?](https://arxiv.org/abs/2412.11385) identifies 21 words whose overrepresentation in scientific abstracts is likely linked to LLM use, including well-known examples such as `delve`, `intricate`, and `underscore`. This supports cluster-level lexical review, but academic vocabulary does not transfer mechanically to fiction.
- [Do LLMs write like humans? Variation in grammatical and rhetorical styles](https://www.pnas.org/doi/10.1073/pnas.2422455122) shows model- and genre-dependent stylistic differences. Use it as a warning against a universal phrase list.

### Field evidence: observed model output and practitioner experience

- [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) is a maintained field guide, not policy. It catalogs high-density AI vocabulary, negative parallelisms, rule-of-three overuse, elegant variation, formulaic em dashes, generic importance claims, and canned transitions. It explicitly warns that individual signs are not proof and that model habits change. Its July 2026 evidence says Claude, unlike other tested contemporary models, still used more em dashes than professional writers.
- A [long-form Claude fiction case report](https://www.reddit.com/r/ClaudeAI/comments/1rb65g7/i_used_claude_to_write_a_301000word_novel_heres/) describes em-dash saturation, repeated participial phrases, `a [noun] that [verbed]`, `seemed to`, `appeared to`, `couldn't help but`, generic emotion naming, and premature conflict resolution. Treat these as Claude-user observations, not measurements.
- A [Claude writers' revision checklist](https://www.reddit.com/r/ClaudeAI/comments/1ub90n3/writers_that_use_claude_are_you_having_issues/) highlights `something about`, `the kind of`, `almost`, `somehow`, `without thinking`, tricolon and fragment stacking, narrated silence, explained subtext, and filler stage direction. These are useful low-to-medium-confidence candidates when repeated.
- [22 Claude Clichés](https://www.linkandth.ink/p/catalog-of-claude-cliches) identifies the aphoristic ender, colon-reveal, suspense hook, theatrical tail clause, stakes-raising, and significance-signaling as recurring Claude structures. It is a close reading of model output rather than a corpus study; use its labels to notice repeated machinery, not to ban compact sentences.
- [Teaching Claude Who You Are](https://www.blog.lituus.studio/blog/teaching-claude-who-you-are) describes repeated false closure as multiple consecutive paragraphs that each feel like an ending. It also flags vague forward-looking final lines, inspirational flourishes, and meta-narration that tells the reader what to feel.
- A user-posted [Claude fiction excerpt](https://www.reddit.com/r/BeyondThePromptAI/comments/1tpqvs6/the_space_between_sessions/) demonstrates several of these devices together: repeated belief statements, `That was the whole of it`, and an `And somehow ... that was enough` final sentence. Treat the example as model-specific field evidence, not a frequency measurement.
- A [Claude fiction prompt shared by a practitioner](https://www.reddit.com/r/ClaudeAI/comments/1fivbml) explicitly asks the model to omit declarative scene endings and long closing narration, suggesting that users encounter the habit often enough to prompt against it.
- The community [Getting AI to Write Good Fiction](https://slop.sus.cat/fiction/ai-fiction-writing/webapp/index.html) catalog aggregates corpus projects and practitioner lists. Use it to broaden candidate discovery, not as authority for its claimed ratios unless the underlying dataset is checked.

## Core decision rule

Do not ask, "Is this phrase on the list?" Ask:

> Is this construction recurring, generic enough to move unchanged into another scene, and substituting polish for a concrete observation or character-specific judgment?

A single exact, earned use is usually clean. Repetition, density, and voice flattening are the signal.

## A. Contrastive scaffolding

### Forms to search

- `It wasn't X. It was Y.` / `It isn't X; it's Y.`
- `This wasn't just X—it was Y.`
- `not just X, but Y` / `not only X, but also Y` / `not merely X, but Y`
- `no X, no Y, just Z`
- `not X so much as Y`
- `less X, more Y`
- `not because X, but because Y`
- `more than X; it was Y`
- repeated negation before the observation: `He didn't smile. He didn't move. He just watched.`

### Flag when

- two or more variants occur per roughly 1,000 words;
- the negated X was never a plausible reader assumption;
- the construction manufactures revelation or drama without adding information; or
- several characters think in the same contrastive cadence.

### Fix

State Y directly, or replace the abstract contrast with the physical fact that makes Y true. Keep antithesis when the opposition is real and the cadence earns emphasis.

## B. Stock fiction phrases

### Corpus-backed candidates

- `voice barely above a whisper`
- `eyes never leaving [object/person]`
- `heart hammered/pounded against [his/her/their] ribs`
- `voice trembling slightly`
- `voice devoid of emotion`
- `felt a profound sense of`
- `something flickered/flashed across [his/her/their] face`
- `a flicker of [emotion] crossed [his/her/their] features`
- `a shiver ran down [his/her/their] spine`
- `the air crackled with [tension/energy]`
- `a wave of [emotion] washed over [him/her/them]`
- `the weight of [emotion/fact] settled on [him/her/them]`
- `the world seemed to stop/slow/fall away`
- `couldn't tear [his/her/their] eyes away`

### Practitioner-observed candidates

- `breath hitched` / `released a breath [they] didn't know [they] were holding`
- `jaw clenched/tightened`
- `eyes widened/narrowed/darkened`
- `the silence stretched/hung/pressed/settled between them`
- `the words hung in the air`
- `quiet determination` / `steel in [his/her/their] voice`
- `ghost of a smile` / `almost a smile` / `not quite a smile`
- `the room suddenly felt smaller`
- `between one heartbeat and the next`
- `the apology [he/she/they] never gave` / `the words [he/she/they] couldn't say`

### Flag when

A phrase repeats, several phrases from this family cluster within a page, or the wording supplies an off-the-shelf emotional cue where the scene already contains a more specific object, action, injury, or relationship detail.

### Fix

Use the character's concrete behavior and the scene's actual sensory environment. A refrigerator hum, a latch tried twice, a thumb worrying a torn seam, or a line of text on a screen can carry silence and emotion without naming either.

## C. Vague pseudo-specificity

### Forms to search

- `something about the way ...`
- `something in [his/her/their] voice/expression/gaze`
- `something shifted/stirred/broke/passed between them`
- `something [he/she/they] couldn't name`
- `the kind of X that Y`
- `almost as if` / `almost like` / `not quite`
- `what might/could have been a smile/laugh/sigh`
- `somehow` / `and somehow, that was worse`
- `a mixture of X and Y` / `somewhere between X and Y`
- abstract body containers: emotion `lived in`, `made a home in`, or sat `behind [the] ribs/sternum`

### Flag when

The sentence signals depth while refusing to name the observed cue. Do not flag genuine POV uncertainty when identifying the cue would give the character knowledge they do not have.

### Fix

Name the visible or audible fact, or commit to the POV character's interpretation. If ambiguity matters, render the competing evidence instead of saying it is ambiguous.

## D. Canned connectors and signposts

### Essay-like connectors

- sentence-opening `Additionally`, `Moreover`, `Furthermore`, `Consequently`, `Nevertheless`, `Notably`, `Indeed`, `Ultimately`
- repeated sentence-opening `However`, `Still`, `Yet`, or `But`
- `On the other hand`, `In contrast`, `By contrast`, `With this in mind`

### Fiction signposts and closures

- `For a moment` / `In that moment`
- `As if on cue`
- `And with that`
- `One thing was clear/certain`
- `Little did [character] know`
- `It was a reminder/testament that ...`
- `This marked/represented a turning point`
- `set the stage for`
- `in the end` / `at the end of the day`
- `the journey ahead` / `what lay ahead`

### Flag when

Three or more explicit connectors occur per roughly 1,000 words, a connector starts consecutive paragraphs, or the signpost announces a transition/emphasis already obvious from sequence. Transition words in isolation are weak evidence.

### Fix

Use chronology, paragraphing, or the next action to create the transition. Delete the signpost when the relationship survives without it.

## E. Hedging and connective filler

### Forms to search

- `seemed to` / `appeared to`
- `couldn't help but`
- `found himself/herself/themselves`
- `without thinking` / `without meaning to` / `without realizing`
- `before [he/she/they] knew it`
- `began to` / `started to` when the action completes
- repeated `as if` / `as though`
- dialogue glue: `turned to face`, `crossed the room`, `took a step`, `shifted in [the] seat` when position does not matter
- participial tail used repeatedly: `..., his voice ...`; `..., her eyes ...`; `..., a [noun] that [verb] ...`

### Flag when

The prose repeatedly delays a completed action, keeps the POV at arm's length, or inserts motion solely to separate dialogue lines. One hedge can encode real uncertainty.

### Fix

Use the direct verb, render the visible hesitation, or remove the stage direction. Preserve starts/stops when interruption is the point.

## F. Template rhythm

### Forms to search

- rule-of-three stacks: `adjective, adjective, and adjective`; three matched clauses; three-item emotional inventories
- fragment triplets: `Gone. Finished. Over.`
- repeated `He [verb]. He [verb]. He [verb].`
- repeated paragraph openings with the same two-word frame
- many paragraphs of similar sentence count and length
- em dashes repeatedly used for a punchline, correction, or `not X—Y` reveal
- paired abstractions or sensory notes: `iron and fear`, `ash and regret`, `rain and ozone`

### Flag when

The device repeats enough for the reader to anticipate its beat. One tricolon or fragment can be excellent. For em dashes, compare against the author's baseline and ignore this novel's bare scene-break line.

### Fix

Keep the strongest item, break the symmetry with a concrete action, or vary sentence length according to pressure. Do not vary mechanically for its own sake.

## G. Explained subtext and synthetic profundity

### Forms to search

- dialogue followed by `what [he/she] meant was ...`, `which was [name]-speak for ...`, or `and they both knew ...`
- action followed by the emotion it already demonstrates
- metaphor followed by an explanation of the metaphor
- `The words landed/hung/cut deeper than ...`
- `It wasn't the words themselves, but ...`
- a paragraph-ending moral, theme, or tidy summary of the beat
- empty significance language: `served as a reminder`, `underscored the importance`, `a testament to`, `marked a pivotal moment`

### Flag when

The second sentence removes productive reader inference or upgrades an ordinary beat into a generalized lesson.

### Fix

Trust the dialogue/action, or replace the explanation with a consequence that changes what the POV character does next.

## H. Lexical clusters

### Research-backed general candidates

`additionally`, `align with`, `bolster`, `crucial`, `delve`, `emphasize`, `enduring`, `enhance`, `foster`, `garner`, `highlight`, `interplay`, `intricate`, `landscape` (abstract), `meticulous`, `pivotal`, `robust`, `showcase`, `tapestry` (abstract), `testament`, `underscore` (figurative), `valuable`, `vibrant`

### Fiction-community candidates

`quietly`, `profound`, `visceral`, `liminal`, `ethereal`, `haunting`, `poignant`, `ineffable`, `transcendent`, `ephemeral`, `gossamer`, `luminous`, `iridescent`, `unwavering`, `indelible`, `shimmer`, `glimmer`, `unfurl`, `smolder`, `radiate`, `crucible`, `realm`, `symphony`, `crescendo`, `veil`

### Flag when

At least three distinct candidates or five total uses cluster in a short passage, especially when they describe importance or emotion without adding imageable detail. Never flag a single word or replace a precise technical/literal use.

### Fix

Replace the abstract modifier with the fact that earns it. Prefer ordinary exact verbs over ornamental synonyms.

## I. Voice flattening

Look for:

- several characters using the same cautious, reflective syntax;
- a practical POV suddenly reaching for abstract literary metaphors;
- uniformly complete, balanced dialogue where interruptions, evasions, and idiolect should differ;
- sudden drift from the established voice into neutral explanatory narration;
- repeated emotional softeners: `kind of`, `somewhat`, `a little`, `perhaps`, `maybe`, `seemed`.

Flag only with a comparison point from the same text, voice guide, or nearby established prose. The replacement must restore that character's vocabulary and rhythm, not generic "better writing."

## J. Over-dramatic landings and false closure

This is primarily a structural, field-observed signal. Claude and ChatGPT often compress the last sentence of a paragraph into a polished verdict, epigram, portent, or miniature trailer line. One good landing is normal fiction. The model-shaped texture emerges when ordinary beats repeatedly receive the cadence of a chapter ending.

### Compact verdicts and aphoristic enders

- `That was the point/difference/truth.`
- `That was the whole of it.` / `That was all.`
- `That was enough.` / `And somehow, that was enough.`
- `And somehow, that was worse/better.`
- `It changed everything.` / `Nothing would ever be the same.`
- `Not a victory. Not yet.` / `Not anymore.` / `Never again.`
- a crowned final abstraction: `The real battle had only begun.` / `The hardest part was still ahead.`
- a neat binary or maxim: `X leaves scars. Y leaves choices.`

### Portent and hindsight tails

- `though [character] didn't know it yet`
- `in ways [character] couldn't yet understand`
- `whether [character] knew it or not`
- `But that would come later.` / `For now, ...`
- `And everything that followed.`
- `They had no idea how right/wrong they were.`

### Manufactured reveal and significance

- `The truth was simple:` / `Only one thing mattered:` followed by a tidy payload
- `The answer had been there all along.`
- `That was when everything changed.`
- a final sentence that translates the image, states the theme, or tells the reader why the preceding beat matters
- repeated paragraph-end fragments, especially after the preceding sentence already landed: `A promise.` / `A warning.` / `A beginning.`

### Flag when

- two or more nearby paragraphs end on compact verdicts, fragments, or reversals;
- the prose lands the same beat twice or three times: image, explanation, then epigram;
- a routine exchange receives chapter-climax weight without changing stakes, knowledge, relationship, or action;
- the ending depends on abstract nouns, unspecified future consequences, invented rankings, or narrator foreknowledge unavailable to the POV;
- deleting the last sentence leaves the paragraph stronger and fully intelligible; or
- several POV characters close paragraphs in the same polished aphoristic voice.

Do not flag solely because a sentence is short, final, dramatic, or contains `enough`. Give genuine chapter hooks, comic tags, threat reveals, irreversible choices, and established character refrains room to land.

### Landing triage

| Question | Usually keep | Usually revise |
|----------|--------------|----------------|
| What changed? | Stakes, knowledge, relationship, choice, or physical situation | Only the narrator's claim that the beat matters |
| What carries the emphasis? | A scene-specific object, action, image, or voiced judgment | An abstract verdict, ranking, portent, or universal maxim |
| What happens if the final sentence is deleted? | The paragraph loses consequence, timing, or character | The paragraph lands earlier and becomes sharper |
| How often does the move recur? | One earned use at a real turn | Two or more nearby landings, or the same closure voice across POVs |
| Does the POV know this? | The conclusion follows from available evidence | Hindsight predicts later importance or future consequences |

### Fix

1. Test deletion first. If the image or action already carries the beat, remove the verdict.
2. Keep one landing, not three. Choose the concrete change with the most consequence.
3. End on an object, action, sensory fact, decision, or unanswered pressure already present in the scene.
4. Replace vague future portent with the immediate consequence the POV can perceive.
5. If an epigram belongs to the character's voice, reserve it for a beat important enough to earn it and vary the surrounding paragraph endings.

## False-positive safeguards

- Human writers originated all of these constructions. Familiarity is not provenance.
- Model versions change; `delve` was strongly associated with older ChatGPT and declined later.
- Claude-specific observations are time-bound and largely anecdotal unless a cited study says otherwise.
- Dramatic paragraph endings are a craft device, not a model signature. Judge repetition, false emphasis, POV access, and whether the sentence adds consequence.
- Non-native English, house style, genre convention, accessibility needs, and deliberate rhetoric can all produce the same surface patterns.
- Perfect grammar, one em dash, one transition word, formal vocabulary, clichés generally, and polished prose are ineffective indicators by themselves.
- Report the craft cost: genericity, repetition, false emphasis, distance, or voice mismatch. If no craft cost exists, do not flag the passage.
