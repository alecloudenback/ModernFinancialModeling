# Feedback Response Plan

Reviewer feedback analysis with proposed actions. Each item is evaluated in context of the actual `.qmd` source. Items marked **ACCEPT** will be edited; **DECLINE** items include justification; **PARTIAL** items adapt the spirit of the feedback.

---

## General Comments

### GC1: Overuse of "something" throughout the book

**Assessment: PARTIAL — address selectively**

The reviewer identifies ~14 instances of "something" and suggests more precise language. I agree in some cases but not all — the book intentionally uses a conversational tone, and some instances are fine. Here's a case-by-case breakdown:

| # | Location | Current text | Recommendation | Action |
|---|----------|-------------|----------------|--------|
| 1 | `foundations-of-programming.qmd:277` | "lets us bind something to a variable" | Replace "something" → "a value" | **ACCEPT** |
| 2 | `foundations-of-programming.qmd:696` | "do something like sum all of the elements" | Fine as-is — "something like" is an idiomatic hedge | **DECLINE** |
| 3 | `foundations-of-programming.qmd:766` | Title "Types for things not there" | Colloquial but clear and memorable as a heading | **DECLINE** |
| 4 | `foundations-of-programming.qmd:770` | "missing is to represent something *should* be there" | Replace "something" → "a value that" | **ACCEPT** |
| 5 | `foundations-of-programming.qmd:1182` | "constructing something from another value" | Replace "constructing something" → "constructing a new value" | **ACCEPT** |
| 6 | `foundations-of-programming.qmd:1307` | "passing something into a function's scope" | Replace "something" → "data" | **ACCEPT** |
| 7 | `first-abstractions.qmd:420` | "sets of things that work with the binary operator" | Replace "sets of things" → "sets of elements" | **ACCEPT** |
| 8 | `first-abstractions.qmd:647` | "A working implementation of something is better than..." | Idiomatic/aphoristic — reads well as-is | **DECLINE** |
| 9 | `software.qmd:596` | "Once you have created something" | Replace "something" → "a package" (contextually it's about distributing packages) | **ACCEPT** |
| 10 | `statistics.qmd:38` | "how much useful data is contained within something" | Replace "within something" → "within a signal or dataset" | **ACCEPT** |
| 11 | `statistics.qmd:883` | "'Strongly informative' priors would be something where" | Replace "would be something where" → "are those where" | **ACCEPT** |
| 12 | `autodiff.qmd:129` | "When performing something like optimization" | Fine as-is — "something like" is an appropriate hedge | **DECLINE** |
| 13 | `optimization.qmd:88` | "the objective function is something we want to minimize" | Replace "is something we want to minimize" → "is a function we want to minimize" | **ACCEPT** |
| 14 | `other-techniques.qmd:29` | "divide by something that's now zero" | Conversational and vivid — reads well as-is | **DECLINE** |

---

### GC2: Julia installation section placement (page 377 / `julia-writing.qmd`)

**Assessment: DECLINE**

**Location:** `julia-writing.qmd:29-71` (Chapter 21 "Writing Julia")

**Justification:** The book is structured so that Parts 2-5 cover conceptual foundations and computational thinking — these are designed to be readable even without hands-on coding. The "Julia Development" part (Part 6, Chapters 21-24) is deliberately the practical "getting your hands dirty" section. The installation instructions are placed here intentionally, alongside environment setup, editors, and debugging workflows. Including installation instructions earlier (e.g., in Part 1) would break the conceptual flow of the early chapters.

However, a brief note or cross-reference early in the book (e.g., in the intro part) pointing readers to Chapter 21 if they want to follow along with code could help. **Consider adding a one-sentence callout in `intro.qmd` or `foundations-of-programming.qmd`** directing eager readers to Ch 21 for setup.

**Proposed action:** Add a brief callout in `foundations-of-programming.qmd` near the start, something like: "To follow along with the code examples interactively, see @sec-julia-setup for installation instructions."

---

### GC3: Overlap between Ch 10/11 and Ch 24

**Assessment: PARTIAL — acknowledge but keep structure**

**Analysis of overlap:**
- Ch 10 (`performance-single.qmd`): Sequential performance patterns — allocations, memory access, type stability, branch prediction
- Ch 11 (`Parallelization.qmd`): Parallelization concepts — SIMD, threading, GPU, multi-processing
- Ch 24 (`julia-optimizing.qmd`): Practical optimization guide — profiling tools, detecting/fixing instabilities, compilation, brief parallelism recap

The overlap is intentional: Ch 10-11 teach the *concepts* (in the "Computational Foundations" part), while Ch 24 is a *practical reference* (in the "Julia Development" part) showing how to use tools like `@code_warntype`, `BenchmarkTools`, profilers, etc.

**However**, the reviewer's specific concern about section 24.9 ("Parallelism") having subsections on multithreading, distributed computing, GPU, and SIMD is valid — this does duplicate Ch 11 content without adding much new tool-oriented content.

**Proposed action:** In Ch 24's parallelism section, trim the subsections to be brief cross-references to Ch 11 rather than re-explanations. Keep only the tool-specific content (e.g., `JULIA_NUM_THREADS`, `MPI.jl` setup) that isn't in Ch 11. Add explicit cross-references like "For the conceptual foundations of multithreading, see @sec-multithreading."

---

### GC4: Sentences needing commas or splitting

**Assessment: ACCEPT most — these are legitimate readability improvements**

| # | Location | Issue | Proposed fix |
|---|----------|-------|-------------|
| 1 | `foundations-of-programming.qmd:526` | "...same amount of bits which will enable..." | Add comma before "which" (non-restrictive clause) |
| 2 | `foundations-of-programming.qmd:546` | "...comprehension syntax which is a convenient..." | Add comma before "which" |
| 3 | `foundations-of-programming.qmd:672` | "...an identifier which cannot be seen..." | This "which" is restrictive (defines which identifiers), so no comma needed. **DECLINE** |
| 4 | `foundations-of-programming.qmd:696` | Long sentence with "which isn't generally the case for a tuple" | Add comma before "which" |
| 5 | `foundations-of-programming.qmd:1144` | "...but do not use position...but instead use named..." | Rewrite to avoid double "but" |
| 6 | `type-abstractions.qmd:236` | Long `mapreduce` callout | Fine as-is — it's a code-heavy callout note, not running prose |
| 7 | `type-abstractions.qmd:305` | "...built this way but in our experience..." | Add comma before "but" (joins two independent clauses) |
| 8 | `performance-single.qmd:58` | "...heap allocated while small fixed size..." | Add comma before "while" |
| 9 | `Parallelization.qmd:686` | "...user-friendliness and uses a primary/worker model wherein..." | Add comma before "and uses" (separates two predicates); add comma before "while" |
| 10 | `elements-of-compsci.qmd:446` | Long footnote | This is fine as a footnote — length is acceptable. **DECLINE** |
| 11 | `statistics.qmd:38` | "...information theory which is the description..." | Add comma before "which" (non-restrictive, defines "information theory") |

---

## Specific Comments

### SC1: Boolean equality notation (p.75)
**Location:** `foundations-of-programming.qmd:152`
**Current:** `true` is equal to `1` (`true == 1`) and `false` is equal to `0` (`false == 0`).
**Feedback:** The parenthetical `(true == 1)` is confusing — strictly it should say "`true == 1` is true."
**Assessment: PARTIAL** — The reviewer has a point about pedantic ambiguity, but the current phrasing is clear enough in context. The parentheticals are just showing the Julia expression, not its result.
**Proposed action:** Rephrase slightly: "`true` is equal to `1` (i.e., `true == 1` evaluates to `true`) and `false` is equal to `0` (i.e., `false == 0` evaluates to `true`)."

Actually, on reflection, the current form is fine — the parentheticals show the *expression*, which is standard notation. **DECLINE** — the existing text is clear in context.

---

### SC2: `const` reassignment (p.78)
**Location:** `foundations-of-programming.qmd:301`
**Current:** "Note that variables can be re-assigned unless they are marked as `const`"
**Feedback:** `const` variables *can* be reassigned interactively (with a warning), as shown in the book's own example.
**Assessment: ACCEPT** — This is a valid technical correction. In Julia, reassigning a `const` in the REPL produces a warning but succeeds (for same-type values). The text should be more precise.
**Proposed action:** Revise to something like: "Note that variables can be freely re-assigned. Marking a variable as `const` signals that it should not be re-assigned and enables compiler optimizations. In an interactive session, Julia will allow reassignment of a `const` with a warning, but in compiled code this is not permitted."

---

### SC3: Repeated loop performance statement (p.80)
**Location:** `foundations-of-programming.qmd:389`
**Current:** "Loops are highly performant in Julia and often the fastest way to accomplish things. This approach contrasts with advice often given to Python or R users, where vectorized operations are heavily favored over loops for performance. In Julia, ⁠for loops are highly performant and often the most efficient and readable way to implement an algorithm."
**Feedback:** First and last sentence say the same thing.
**Assessment: ACCEPT** — Clear redundancy. Remove the last sentence or merge.
**Proposed action:** Revise to: "Loops are highly performant in Julia and often the fastest way to accomplish things. This contrasts with advice often given to Python or R users, where vectorized operations are heavily favored over loops for performance."

---

### SC4: "Collections are really useful" (p.84)
**Location:** `foundations-of-programming.qmd:510`
**Current:** "Collections are types that are really useful for storing data which contains many elements."
**Feedback:** "are really useful" is filler — collections *are* the way to store multiple elements.
**Assessment: ACCEPT**
**Proposed action:** "Collections are types for storing data that contains many elements."

---

### SC5: Circular range definition (p.87)
**Location:** `foundations-of-programming.qmd:607`
**Current:** "A **range** is a representation of a range of numbers."
**Feedback:** Circular — use "sequence" instead.
**Assessment: ACCEPT**
**Proposed action:** "A **range** is a compact representation of a sequence of numbers."

---

### SC6: Tuple definition (p.89)
**Location:** `foundations-of-programming.qmd:676`
**Current:** "Tuples are a set of values that belong together"
**Feedback:** "belong together" is vague.
**Assessment: PARTIAL** — "belong together" is intentionally informal but could be slightly more precise.
**Proposed action:** "Tuples are a fixed, ordered collection of values" — and add a note that tuples should generally be used for small collections (as the reviewer suggests, since this is only clarified much later).

---

### SC7: "Three value logic" caption (p.92)
**Location:** `foundations-of-programming.qmd:796`
**Current:** "Three value logic with `true`, `missing`, and `false`."
**Feedback:** Comes out of the blue.
**Assessment: PARTIAL** — It's a table caption (`#tbl-third`), so it's meant to be terse. But it could use a brief lead-in sentence before the table.
**Proposed action:** Check if there's already a lead-in sentence before the table. If not, add one like: "The following tables show how `missing` interacts with standard boolean operations in Julia's three-value logic:" (this may already exist in the OR/AND/NOT table series).

---

### SC8: "types types" double word (p.94)
**Location:** `foundations-of-programming.qmd:891`
**Current:** "The above `struct`s that we have defined are examples of **concrete types**`\index{concrete type}`{=latex} types which hold data."
**Feedback:** "types" appears twice.
**Assessment: ACCEPT** — Clear typo/duplication introduced by the index marker.
**Proposed action:** Fix to: "...are examples of **concrete types**`\index{concrete type}`{=latex} which hold data." (remove the extra "types")

---

### SC9: Method vs method instance distinction (p.97)
**Location:** `type-abstractions.qmd` (methods section)
**Feedback:** Maybe introduce distinction between "method" and "method instance."
**Assessment: DECLINE** — Julia's own documentation uses "method" consistently. Introducing "method instance" would be non-standard terminology that could confuse readers who later consult Julia docs. The existing explanation of functions having multiple methods is already clear.

---

### SC10: "happen at the same time" re: fusing (p.102)
**Location:** `foundations-of-programming.qmd:1237`
**Current:** "When it's fused, the operations can happen at the same time without creating an interim set of values."
**Feedback:** "at the same time" could imply parallelism.
**Assessment: ACCEPT** — Good catch; fusing is about avoiding intermediate allocations, not about concurrency.
**Proposed action:** Replace "can happen at the same time" → "are combined into a single pass over the data" or "are applied element-by-element in a single pass."

---

### SC11: `reduce` explanation (p.119)
**Location:** `first-abstractions.qmd:425`
**Current:** "`reduce` takes an operation and a collection and applies the operation repeatedly to pairs of elements until there is only a single value left."
**Feedback:** Should mention accumulator variable.
**Assessment: PARTIAL** — The current definition is accurate to how `reduce` works conceptually. Mentioning an "accumulator" could be helpful, but adding too much detail here front-loads complexity.
**Proposed action:** Add a brief clarification: "`reduce` takes an operation and a collection and applies the operation repeatedly — combining elements pairwise, carrying forward the intermediate result — until there is only a single value left."

---

### SC12: Multiple Collections section placement (p.122)
**Location:** `first-abstractions.qmd:583` (section 6.4.6.2 "Multiple Collections")
**Feedback:** Should be in section 6.4.1 (map).
**Assessment: DECLINE** — The "Multiple Collections" section applies to `map`, `reduce`, and the other functional operators in section 6.4, not just `map`. Its current placement after all the individual operators makes sense as a cross-cutting note.

---

### SC13: "right method" → "corresponding method" (p.132)
**Location:** `type-abstractions.qmd:145`
**Current:** "Dispatch is the process of determining the right method to use"
**Feedback:** "right" → "corresponding" or rephrase.
**Assessment: ACCEPT** — "corresponding" is more precise.
**Proposed action:** "Dispatch is the process of determining which method to use"

---

### SC14: Unreadable note on page 142
**Location:** `type-abstractions.qmd` ~line 345-355
**Assessment:** Looking at the source, this appears to be the side-by-side column layout comparing JuliaInsurance.jl vs pyInsurance. The `::: {.column width="4%"}` creates a spacer, and the columns are 43% and 53%. This is a PDF rendering issue where the column layout may clip content.
**Proposed action:** Check the PDF rendering of the side-by-side columns around line 340-385 of `type-abstractions.qmd`. The Quarto column layout may need width adjustments for the 7"×10" page format. **Flag for PDF review.**

---

### SC15: Table readability — Encapsulation row (p.146)
**Location:** `patterns-abstraction.qmd:32`
**Current:** "Don't let other parts of the program modify internal data and make the system easier to understand and maintain."
**Feedback:** Reads like "Don't let other parts of the program make the system easier..."
**Assessment: ACCEPT** — The sentence has a dangling modifier / ambiguous conjunction.
**Proposed action:** Split into two goals: "Hide internal data from other parts of the program. Make the system easier to understand and maintain." Or rephrase: "Prevent other parts of the program from modifying internal data, making the system easier to understand and maintain."

---

### SC16: Homoiconicity recipe analogy (p.152)
**Location:** `patterns-abstraction.qmd:218`
**Feedback:** The recipe analogy is confusing — "the code (the recipe) can also be treated as data to be manipulated" sounds like a recipe is used as a recipe.
**Assessment: PARTIAL** — The analogy is actually: you can *follow* a recipe (execute code) OR you can *analyze/modify* the recipe text itself (treat code as data). The confusion may stem from brevity.
**Proposed action:** Slightly expand the analogy to make the two uses clearer: "You can follow the recipe's instructions (execute the code) to bake a cake. But you could also treat the recipe itself as data to be manipulated: you could write a program to scan thousands of recipes, find every instance of 'sugar,' and reduce the quantity by 25%. This is the essence of homoiconicity: the same representation serves both as executable instructions and as data that can be inspected or transformed."

---

### SC17: expm1/log1p slash notation (p.169)
**Location:** `hardware.qmd:282`
**Current:** "For small r, use `expm1`/`log1p` to improve accuracy"
**Feedback:** "/" could be misinterpreted as division.
**Assessment: ACCEPT** — Easy fix.
**Proposed action:** Change to: "For small r, use `expm1` and `log1p` to improve accuracy"

---

### SC18: "Secondly" without "Firstly" (p.171)
**Location:** `performance-single.qmd:24`
**Current:** "However, writing correct, performant parallel code relies on understanding efficient sequential patterns first. Secondly, many problems are not 'massively parallelizable'..."
**Feedback:** No "Firstly" to match.
**Assessment: ACCEPT** — The implicit "first" is in "...first" at the end of the prior sentence, but the jump to "Secondly" is jarring.
**Proposed action:** Change "Secondly," to "Additionally," or "Moreover," since the "first" reason is embedded in the prior sentence.

---

### SC19: Type instability definition scope (p.177)
**Location:** `performance-single.qmd:233`
**Current:** "To avoid type instabilities, ensure that functions have inferrable, concrete types across all code paths."
**Feedback:** Should mention that variables should be local; someone might think a typed global `x = 2` is fine.
**Assessment: PARTIAL** — The reviewer makes a good point, but this is addressed nearby in Ch 24 (`julia-optimizing.qmd:41-51`) where global variables are discussed. However, a brief addition here would help.
**Proposed action:** Add a brief note after the sentence: "This includes ensuring that all variables used within functions are either local or passed as arguments — accessing global variables from within a function inhibits type inference (see also @sec-type-inference)."

---

### SC20: S(n) equation out of the blue (p.181)
**Location:** `Parallelization.qmd:30-37` (Amdahl's Law)
**Feedback:** The equation is introduced without context.
**Assessment:** Looking at the source, the equation appears under the heading "## Amdahl's Law and the Limits of Parallel Computing" with surrounding text. The "page 181" reference may be a pagination artifact. Let me check the lead-in.
**Proposed action:** Verify the paragraph before the equation provides adequate context. If the equation follows immediately after a heading without a lead-in sentence, add one like "Amdahl's Law quantifies this limit. The theoretical speedup is given by:"

---

### SC21: Warning output on page 182
**Location:** Likely `Parallelization.qmd` or `performance-single.qmd` — a Julia code cell producing a warning in the rendered output.
**Assessment:** This is a rendered output issue — a Julia code cell is producing a warning message that shows up in the PDF. Need to identify the specific cell and either fix the warning or suppress it with `#| warning: false`.
**Proposed action:** **Flag for build review** — identify and fix the warning-producing cell.

---

### SC22: "indexing an array is actually a branch" (p.184)
**Location:** `Parallelization.qmd:107`
**Current:** "Note that indexing an array is actually a branch in the code"
**Feedback:** "is" → "introduces"?
**Assessment: ACCEPT** — "introduces" is more precise.
**Proposed action:** "Note that indexing an array actually introduces a branch in the code"

---

### SC23: SIMD safety note (p.185)
**Location:** `Parallelization.qmd:147`
**Current:** "SIMD isn't prone to issues like this because if the code is not SIMD-able then the compiler will not auto-vectorize the code block."
**Feedback:** This is true for `@simd` but not for `@turbo` (LoopVectorization.jl), which can give incorrect results for dependent iterations like `x[i] = x[i-1]`.
**Assessment: ACCEPT** — Valid and important caveat.
**Proposed action:** Add a sentence: "Note that this safety guarantee applies to Julia's built-in `@simd` macro. Third-party macros like `@turbo` (from LoopVectorization.jl) are more aggressive and may produce incorrect results if loop iterations have data dependencies (e.g., `x[i] = x[i-1]`)."

---

### SC24: "not unlike vectorization" (p.193)
**Location:** `Parallelization.qmd:449`
**Current:** "The GPU cores essentially have to be running the same set of instructions on all of the data, not unlike vectorization"
**Feedback:** Typo?
**Assessment: DECLINE** — "not unlike" is an intentional litotes (double negative for emphasis), meaning "similar to." It's a common English construction. Not a typo.

---

### SC25: Missing space "tmapreduce,tcollect" (p.203)
**Location:** `Parallelization.qmd:776`
**Current:** `tmapreduce`,`tcollect`
**Assessment: ACCEPT** — Missing space after comma.
**Proposed action:** Add space: `` `tmapreduce`, `tcollect` ``

---

### SC26: Errors in output pages 206-209
**Assessment:** These are rendered output errors from Julia code cells in `Parallelization.qmd`. Like SC21, these are build/execution issues.
**Proposed action:** **Flag for build review** — re-render the parallelization chapter and fix any code cells producing errors.

---

### SC27: "An aggregate of named fields" out of the blue (p.248)
**Location:** `elements-of-compsci.qmd:480-481`
**Current section starts:** "An aggregate of named fields, typically of fixed size and sequence."
**Feedback:** Starts abruptly.
**Assessment: ACCEPT** — The section heading is "Records/Structs" but the first sentence reads like a dictionary definition dropped in.
**Proposed action:** Add a brief intro: "A **record** (or `struct` in Julia) is an aggregate of named fields, typically of fixed size and sequence."

---

### SC28: Confidence interval explanation (p.271)
**Location:** `statistics.qmd:554`
**Current:** "An X% confidence interval refers to a procedure that results in a range R wherein X% of the time the true value of interest lies within R."
**Feedback:** Confusing phrase.
**Assessment: PARTIAL** — This is actually the *correct* frequentist definition (it's about the procedure, not any single interval). The confusion may be inherent to the concept. However, wording could be slightly improved.
**Proposed action:** Rephrase for clarity: "An X% confidence interval comes from a procedure that, if repeated many times, would produce intervals containing the true value X% of the time." Or keep as-is since the surrounding text explains the FCF (Fundamental Confidence Fallacy).

---

### SC29: Dual numbers benchmark presentation (p.315-318)
**Location:** `autodiff.qmd:275-286`
**Current:** Shows `@btime f3(x)` vs `@btime f3(DualNumber(x, 1))`, then says "we effectively are able to compute the function and its derivative at less than two times the cost."
**Feedback:** The AD version is slower in the benchmark, but the text reads like it's suggesting it's faster. Confusing.
**Assessment: ACCEPT** — The text *is* saying it's remarkably cheap (less than 2x cost for getting both value AND derivative), but the framing could be clearer that we're comparing "one evaluation" vs "one evaluation that also gives you the derivative for free."
**Proposed action:** Rephrase to be more explicit: "The dual number version takes somewhat longer than the plain function evaluation — but notice that for this additional cost, we get both the function value *and* its exact derivative. This is typically less than twice the cost of the base evaluation alone. Compare this to finite differences, which require two or three separate function evaluations just to *approximate* the derivative."

---

### SC30: Code snippet introduced out of the blue (p.316)
**Location:** `autodiff.qmd:298-324` (Black-Scholes example)
**Assessment:** This is the `eurocall` function used in the "Automatic Differentiation in Practice" section. Looking at the source, the section starts with explanatory text at line 294-296 before the code. This should be adequate context.
**Proposed action:** Check that the transition from the performance discussion to the Black-Scholes example has a clear lead-in sentence. The current text at line 294 ("We have, of course, not defined an exhaustive list of operations...") does lead into the practical example. **Likely OK — verify in PDF.**

---

### SC31: "Analytic derivatives" recap mismatch (p.324)
**Location:** `optimization.qmd:112`
**Current:** Lists "Analytic derivatives" as a recap item from Chapter 16.
**Feedback:** Can't find "Analytic derivatives" mentioned in Chapter 16 (autodiff.qmd).
**Assessment:** Looking at the source, `optimization.qmd:110` says "a quick recap of the available approaches" and lists finite differences, analytic derivatives, and AD. This is a recap of derivative *methods* in general, not necessarily all from Ch 16. The "analytic derivatives" entry says "A human-derived or computer tool (such as Mathematica)..." which is a general method not covered in Ch 16.
**Proposed action:** Rephrase the intro to not imply all items were in Ch 16: "Calculating gradients in the context of computer algorithms is discussed at length in @sec-autodiff. Here is a quick recap of the main approaches to computing derivatives:" (removing the implication that all are from Ch 16).

---

### SC32: Table formatting issue (p.386)
**Location:** `julia-writing.qmd:405-437`
**Feedback:** Table seems to be missing a column for the first entry.
**Assessment:** The table uses Quarto's grid table format (`+----+---+`) which can be finicky in PDF rendering. This is likely a PDF rendering bug.
**Proposed action:** **Flag for PDF review** — check the grid table rendering in the PDF. May need to switch to a pipe table or adjust column widths.

---

### SC33: Artifact system sentence (p.386)
**Location:** `julia-writing.qmd` (Artifacts section)
**Feedback:** "The artifact system is used to download and verify the contents of a file match the hash" is confusing.
**Proposed action:** Search for this exact text, rephrase for clarity. Likely: "The artifact system downloads files and verifies that their contents match a known hash."

---

### SC34: "Click left" → "Click to the left" (p.401)
**Location:** `julia-debugging.qmd:238`
**Current:** "Click left of a line number"
**Assessment: ACCEPT**
**Proposed action:** "Click to the left of a line number"

---

### SC35: Type inference and functions (p.411)
**Location:** `julia-optimizing.qmd:24-51`
**Feedback:** Should clarify that type inference operates within functions; the examples imply it but never state it explicitly.
**Assessment: ACCEPT** — Adding one explicit sentence would help.
**Proposed action:** Add after the definition: "Type inference in Julia operates at the function level — outside of functions (e.g., at the REPL or in global scope), Julia does not attempt to infer types in the same way."

---

### SC36: "untyped global variables" (p.411)
**Location:** `julia-optimizing.qmd:41`
**Current:** "the most common beginner pitfall is the use of untyped global variables"
**Feedback:** "untyped" is misleading — even typed globals don't restore full performance (need `const` or local).
**Assessment: ACCEPT** — Good catch. The word "untyped" implies that typing the global would fix it, which isn't true.
**Proposed action:** Change "untyped global variables" to "non-constant global variables" and add a brief note: "Even a type-annotated global variable does not enable the same optimizations as a local variable or a `const`."

---

### SC37: Type stability definition (p.415)
**Location:** `julia-optimizing.qmd:141-156`
**Current:** "For a section of code to be considered type stable, the type inferred by the compiler must be 'concrete'"
**Feedback:** (1) `Vector{Real}` is concrete but slow; (2) "a section of code" should be "a function."
**Assessment: ACCEPT** — Both points are valid. The text already has a callout about `Vector{Real}`, but the definition itself is misleading.
**Proposed action:** Revise definition: "A function is **type stable** when the compiler can infer a concrete return type from the types of the inputs alone." Then keep the existing callout about `Vector{Real}` which already notes the element-type subtlety.

---

### SC38: "Type stability is contagious" (p.415)
**Location:** `julia-optimizing.qmd:157`
**Current:** "Type stability is contagious: if a variable's type cannot be inferred, then the types of variables that depend on it may not be inferrable either."
**Feedback:** Too broad — barrier functions exist to break the chain.
**Assessment: PARTIAL** — The statement is true as a general principle. Barrier functions are an advanced technique that is covered elsewhere. Adding a hedge is fine.
**Proposed action:** Append: "Type stability is contagious: if a variable's type cannot be inferred, then the types of variables that depend on it may not be inferrable either. (In advanced cases, 'function barriers' can be used to contain instability; see Julia's performance tips documentation.)"

---

## Summary of Actions

### Edits to make (by file):

**`foundations-of-programming.qmd`** (11 edits):
1. Line 277: "something" → "a value"
2. Line 389: Remove redundant last sentence about loop performance
3. Line 510: Remove "are really useful"
4. Line 526: Add comma before "which"
5. Line 546: Add comma before "which"
6. Line 607: "representation of a range" → "compact representation of a sequence"
7. Line 676: Revise tuple definition + add small-collection note
8. Line 770: "something" → "a value that"
9. Line 891: Remove duplicate "types"
10. Line 1182: "constructing something" → "constructing a new value"
11. Line 1237: "happen at the same time" → "are combined into a single pass"
12. Line 1307: "something" → "data"

**`first-abstractions.qmd`** (2 edits):
1. Line 420: "sets of things" → "sets of elements"
2. Line 425: Expand `reduce` description slightly

**`type-abstractions.qmd`** (2 edits):
1. Line 145: "right method" → "which method"
2. Line 305: Add comma before "but"

**`patterns-abstraction.qmd`** (2 edits):
1. Line 32: Fix encapsulation table cell ambiguity
2. Line 218: Expand homoiconicity analogy slightly

**`hardware.qmd`** (1 edit):
1. Line 282: "/" → "and"

**`performance-single.qmd`** (3 edits):
1. Line 24: "Secondly" → "Additionally"
2. Line 58: Add comma before "while"
3. Line 233: Add note about local variables

**`Parallelization.qmd`** (3 edits):
1. Line 107: "is actually" → "introduces"
2. Line 147: Add `@turbo` caveat
3. Line 776: Add missing space

**`elements-of-compsci.qmd`** (1 edit):
1. Line 480: Add introductory phrasing

**`statistics.qmd`** (2 edits):
1. Line 38: Improve "something" and add comma
2. Line 883: "would be something where" → "are those where"

**`autodiff.qmd`** (1 edit):
1. Line 286: Clarify benchmark comparison framing

**`optimization.qmd`** (2 edits):
1. Line 88: "something we want" → "a function we want"
2. Line 110: Rephrase recap intro

**`software.qmd`** (1 edit):
1. Line 596: "something" → "a package"

**`julia-optimizing.qmd`** (4 edits):
1. Lines 24-34: Add note about function-level inference
2. Line 41: "untyped global" → "non-constant global"
3. Line 141: Revise type stability definition
4. Line 157: Add barrier function hedge

**`julia-debugging.qmd`** (1 edit):
1. Line 238: "Click left" → "Click to the left"

### Items to flag for PDF/build review:
- SC14: Side-by-side column layout in `type-abstractions.qmd` ~line 340
- SC21: Warning output in parallelization chapter
- SC26: Error outputs pages 206-209
- SC30: Code snippet transition in autodiff.qmd
- SC32: Grid table rendering in `julia-writing.qmd:405`

### Items to investigate further:
- GC2: Consider adding cross-reference to installation chapter from early chapters
- GC3: Trim Ch 24 parallelism section to cross-references
- SC33: Find and rephrase artifact system sentence in julia-writing.qmd
