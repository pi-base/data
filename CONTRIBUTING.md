You'll need to log in or [join GitHub](https://www.github.com/join/) to contribute.

## Discussions

Not sure where to begin? Head over to our [Discussion board](https://github.com/pi-base/data/discussions) and start a new thread!
We're always happy to have new community members join the conversation.

[Here is the thread for discussing these guidelines in particular.](https://github.com/pi-base/data/discussions/322)

## Opening an Issue

If you have a specific improvement you'd like to see made to the pi-Base, you can always
[open an Issue](https://github.com/pi-base/data/issues) that includes the following information:

- All spaces/properties/theorems related to your improvement, including their IDs (e.g. S012345).
  Links to <https://topology.pi-base.org> are encouraged.
- A description of the changes you'd recommend.

After discussion of your suggestion, any contributor can make a "Pull Request" (see below) to
implement your improvement. 

## Make a Pull Request

To add a pull request implementing any changes to the repository, [fork](https://github.com/pi-base/data/fork)
this project to your own account, which creates a copy of <https://github.com/pi-base/data/> to
something like <https://github.com/StevenClontz/pibase-data/>.

The easiest way to edit your fork of the repository is to use GitHub.**dev**.
For example, if your fork is located at <https://github.com/StevenClontz/pibase-data>, you can either edit the URL to say
<https://github.dev/StevenClontz/pibase-data> (note the `.dev`), or press the period key on your physical keyboard
while viewing the repository to be redirected automatically. This opens a file editor in your web browser where you can make
whatever changes you'd like. 

It's good to change the branch name from `main` to something like
`UserName/describe-your-contribution`. (Please do not use the `|` character or anything else
that is not allowed in a Windows filename.)
Then you can "commit & push" your changes to that branch on your fork.

![image](https://github.com/pi-base/data/assets/1559632/3306fed3-9ac0-4b47-845b-feb6b324dc5f)

When editing, be sure to review [our conventions](https://github.com/pi-base/data#conventions) on notation
and naming, and read below on information about references, our review criteria, etc.

Once you're happy with your changes, you can
[open up all pull request for review](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).
Then one of our volunteer reviewers will check your work and discuss the proposed changes
and any required effort necessary before they can be merged into the main data repository.

After you've made one or two contributions, you will likely be invited to make branches directly
on the pi-base/data repository, so they are available to preview using https://topology.pi-base.org/dev

## Labels

We encourage the use of labels for pull requests and issues. Namely, if you add a space, it is good to add the ```space``` label and so on.

The ```easy``` label is meant for pull requests that can be reviewed quickly, for example: Fixing typos, add some simple traits, add a theorem which is immediate from the definitions, etc..
In particular, the ```easy``` should **not** be applied when adding a new space or property or some proof needs outside reading (i.e. references a paper).

## References

Contributions should generally reference a peer-reviewed publication, along with a Mathematical Reviews link
or DOI link. Sometimes Wikipedia references are also appropriate.
The recommended form of reference to a publication is [zbMath](https://zbmath.org/) link.

pi-Base is not a forum for peer review, so
to contribute improvements not directly reflected in the literature, we encourage you to ask (and self-answer
if necessary) an appropriate question on either <https://math.stackexchange.com/> or <https://mathoverflow.net/>,
and use that as your citation.

## Reviewers

Once you have been invited to help maintain the pi-Base (usually after one or two accepted pull requests)
you are also welcome to help review new contributions!

Info for reviewers is at [this page](https://github.com/pi-base/data/wiki/Reviewing). 

## Licensing

The copyright of all data in this repository
is owned by Steven Clontz and James Dabbs and licensed for free public use under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). By contributing to the pi-Base,
you agree that you grant Steven Clontz and James Dabbs an unlimited non-exclusive license
to use your contribution as part of the pi-Base data repository.
Please see [LICENSE.md](https://github.com/pi-base/data/blob/master/LICENSE.md) for details.

# AI Policy

The $\pi$-Base community has adopted the following policy on the use of AI/LLMs (adapted from [mathlib](https://leanprover-community.github.io/contribute/index.html#use-of-ai)'s policy):

Using artificial intelligence tools to generate code is becoming more and more common. While this can be practical, their use also poses ethical, ecological, legal and social concerns. We recognise that there are strong differences in opinion on this topic, and do not enforce a strict ban. That said, while individual action alone will not address these concerns, we ask you to consider the effects of your AI use and if it is truly necessary.

If you use artificial intelligence (such as, by using github's copilot mode, asking an LLM like ChatGPT or using an agent like Codex, Claude or Gemini), please explain this in the PR description. Explain which tool(s) you used and how you used it. This provides useful context for reviewers: tools make different mistakes than humans, so knowing this makes it easier to spot common errors.

In particular, submissions that are the unedited output of an AI tool will be closed without review. These tools should be used only to provide a starting point for a contribution, or possibly to help with editing. However, contributions should ultimately be the work of a human who understands and can vouch for their work.


# Conventions and Style

# Notation

In property descriptions and in proofs of theorems, we often use $X$ to implicitly denote the space being discussed.

When providing the proof of a theorem, for example `A + B implies C`, we usually make the implicit assumption that the hypotheses, `A` and `B` in the example, hold for the space $X$.  So there is usually no need to explicitly state it up front.

# Separation axioms

For the separation axioms, `T_n ⇒ T_m` whenever `n ≥ m`. 
For example [regular](https://github.com/pi-base/data/blob/master/properties/P000011.md)
is defined to assert that closed points and sets can be separated;
[T₃](https://github.com/pi-base/data/blob/master/properties/P000005.md) is defined to be both `regular` and `T₀`. 
See e.g. [wikipedia](https://en.wikipedia.org/wiki/Separation_axiom#Main_definitions) for more information.

# Local Properties

A property is "locally `P`" if every point in the space has a neighborhood base satisfying P for every member of the base. On the other hand, some authors define "locally `P`" to mean there is a single neighborhood satisfying `P` for each point. These definitions are occasionally equivalent (e.g. locally metrizable), but are not equivalent in general (e.g. locally compact). See [this issue](https://github.com/pi-base/data/issues/42) for discussion.

Use "locally P" when the P neighborhoods form a neighborhood base, and (when not equivalent) use "weakly locally P" when only a single P neighborhood is required.

# Meta-properties

At this moment $\pi$-Base does not support *meta-properties* but we collect them on property pages for the use in proofs and also for the visitors as additional mathematical facts. Below you can find the list of currently tracked meta-properties and their standardized phrasing:

1. This property is hereditary.
1. This property is hereditary with respect to open sets.
1. This property is hereditary with respect to closed sets.

1. $X$ satisfies this property iff its Kolmogorov quotient $\mathrm{Kol}(X)$ does.
1. This property is preserved by quotient maps.

1. This property is preserved by arbitrary disjoint unions.
1. This property is preserved by $\Sigma$-products
1. This property is preserved by countable products.
1. This property is preserved by arbitrary products.
1. An arbitrary product of nonempty spaces satisfies this property iff each of its factors does.

1. This property is preserved in any finer topology.
1. This property is preserved in any coarser topology.

1. If each point has a neighborhood with the property, $X$ also has the property.
1. If $X$ is covered by countably many subspaces, each having the property, then so does $X$.

1. If each path component of $X$ has the property, then so does $X$.

If the justification is non-trivial, it is good to provide a reference (in parentheses after the meta-property).  If the justification is straightforward, there is no need to provide one.

On some occasions analogous negative statements (e.g. *This property is not hereditary with respect to open sets*) may be of interest.
Of course whenever a property is said to be hereditary with respect to e.g. open sets, it usually means it is not hereditary in general.

*Note that the list may not be complete; contributors are invited to expand it.*

See also the thread [#1071](https://github.com/pi-base/data/issues/1071).

# Notation advice

- Whenever dealing with intervals and **pairs** (tuples), the latter should be better denoted by $\langle x, y\rangle$ (`\langle` and `rangle`) than $(x,y)$.
If there is no need to care about the intervals, standard pair notation can be used.
- For open covers the `\mathscr` font is commonly used.

# References

When referencing the literature we shall use **zbMath** links whenever possible, especially when the zbMath entry provides the DOI.
Appropriate modification of old files is advised (upon editing them);
e.g. the reference to *Counterexamples in topology* should be switched from the DOI to `zb:0386.54001`.
Note that this requires change in the `refs` header and the links in text `{{doi: ... }}`.


# Reviewing

## Managing pull request branches

Currently the pi-Base automatically compiles a preview of each branch on the `pi-base/data` repository.
This does not include branches opened on forks of the repository (to prevent compiling untrusted data which
could have unwanted or illegal content). So after a pull request is seen to be legitimate, a reviewer
may duplicate the content of a pull request to a new branch via these steps.

First, use GitHub.dev to open the pull request.

![image](https://github.com/pi-base/data/assets/1559632/1d3446a9-ae93-45d1-b815-17ca87de5e9a)

![image](https://github.com/pi-base/data/assets/1559632/b72ad1a2-a7eb-4a9f-b851-e4446297d239)

Then use the bottom toolbar to create a new branch based on the PR.

![image](https://github.com/pi-base/data/assets/1559632/a5a1e93f-da85-4b4a-a6c7-b286cdf56b6e)

Back at github.com you can see the new branch and confirm it compiled.

![image](https://github.com/pi-base/data/assets/1559632/6992fd49-87f9-4e2f-b557-6a60845d8369)

![image](https://github.com/pi-base/data/assets/1559632/4aa18441-d3f0-4ddb-93c7-b8310dd13dc8)

You can now also use the new branch name you created to preview the pull request at
https://topology.pi-base.org/dev

- If that doesn't work, try replacing the "Host" URL with
  `https://pi-base-bundles.s3.us-east-2.amazonaws.com` instead.

![image](https://github.com/pi-base/data/assets/1559632/7a7e425c-3930-4b90-b449-2140afe72850)

![image](https://github.com/pi-base/data/assets/1559632/2e1f838a-d449-46b1-b5ed-54ba26cc1fe6)

At this point, you can approve and merge the original pull request, request that the contributor
make changes to their pull request, or close their pull request and re-open a new pull request
with the branch owned by pi-base to continue the contribution there (where it will be
built and previewed).

## Reviewing Checklist

The golden rules:

- New volunteers should be especially encouraged and thanked for their contributions.
- Contributions that add verifiable mathematical knowledge to the pi-Base with appropriate
  references should be merged as soon as possible.
  - If the PR could nonetheless could be improved (e.g. a better choice of naming, a more
    useful description), those improvements should be proposed in a separate issue/PR
    (whether by encouraging the original contributor, or directly by the reviewer).
  - If the result is not directly addressed by a source, it can be proven in the description
    provided that the proof is immediate. Otherwise, opening a Q&A on e.g. Math.StackExchange
    is likely appropriate (and that `mathse` reference should be used on $\pi$-Base).
- If minor errors (e.g. typos) are found, the reviewer can edit the PR
  directly before accepting and merging the PR.

Contributions that edit/add a "trait" (pair of an existing space/property) are typically acceptable
unless the trait is already deduced by existing theorems.

Since there are infinitely-many possible spaces and properties, the introduction of new spaces and
properties have a higher bar to meet. Likewise, we have some requirements on new theorems in order
to ensure high-quality automated deductions.

### Requirements for a new property

- The property should be of interest to researchers, whether it appears in the peer-reviewed literature
  or another scholarly venue such as MathOverflow.
- If the definition of a property depends on other properties, they should be cited using `{Pxyz}` in
  the description, assuming they exist. If they don't exist, these other properties should be
  added before or alongside the new property.
- The contribution should also include added traits and/or theorems that allows the pi-Base to deduce
  whether or not this property holds for multiple spaces (or there should be plans to do so in future
  contributions).

### Requirements for a new space

At least one of the folowing should be satisfied.

- The space is of interest to researchers, preferably appearing in a textbook or
  the peer-reviewed literature.
- The space provides an example/counter-example that is not currently represented
  in the pi-Base (e.g. it is a space that is X and Y but not Z, and the pi-Base does not already
  know of such an example). So the contribution should include sufficient traits/theorems to
  provide this.
- The space provides a convenient characterization of another space (e.g. [S199](https://topology.pi-base.org/spaces/S000199)
  was introduced to define [S44](https://topology.pi-base.org/spaces/S000044) as a product).

### Requirements for a new theorem

- The thoerem should be of the form `AND(list of props) => prop`.
  - Tip: a theorem of the form `P or Q => R` can be split into two theorems `P => R` and `Q => R`.
    Likewise `P => Q or R` and be rewritten as `P and ~Q => R`, and so on.
- The theorem should not be deducible from existing theorems.
  - Tip: if the theorem `P and Q => R` can be deduced, a search for `P and Q and ~R` in pi-Base
    will point this out.
- If a new theorem makes other theorems redundant, consider whether the other theorems should instead
  be edited to be generalized.
- We like for theorems to be generalized when possible (e.g. assume regular, not $T_3$). But this
  should be considered on balance with usage in the literature (if the result is only cared about in
  the context of "assume all spaces are Hausdorff", then it's fine to have the technically weaker result).
  - Put another way, it's okay to accept a contribution of "$T_3$ and P implies Q" even when the result
    could be improved to "regular and P implies Q". But this does not mean we should reject a later
    improvement of the result to say "regular and P implies Q" if a contributor suggests doing so.



