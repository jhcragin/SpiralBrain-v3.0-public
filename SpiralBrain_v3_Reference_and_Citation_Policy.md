SpiralBrain v3.0 — Introduction & Citation Reference (Canonical)
1. First-mention definition (mandatory)
When SpiralBrain or SpiralBrain v3.0 is first introduced in any paper, it must be defined explicitly as a system and anchored to its public artifact.
Canonical example sentence (recommended):
SpiralBrain v3.0 (Cragin, 2026c) is a Python-based neurosymbolic Regulatory Intelligence (RI) system that runs locally on standard hardware (e.g., a laptop) and exposes internal regulatory metrics for inspection.
This definition:
•	identifies SpiralBrain as an instrumented system, not a benchmark model,
•	states execution constraints (local, standard hardware),
•	signals inspectability (internal metrics),
•	anchors provenance,
•	avoids expanding claim scope.
First architectural mention citation rule:
\cite{SpiralBrainV3,Cragin2026RI}
________________________________________
2. Naming consistency (mandatory)
Use exactly:
SpiralBrain v3.0
•	no hyphen
•	capital B
•	lowercase v
Avoid:
•	Spiralbrain v3.0
•	Spiral-Brain v3.0
•	line-break variants
Reviewers notice this immediately.
________________________________________
3. Bibliography style assumption
All entries below assume:
\bibliographystyle{plain}
\bibliography{references}
Because plain ignores url and doi fields, all visible links are placed in the note field using \url{…}. This is intentional and consistent.
________________________________________
4. Canonical citation blocks (use as needed)
4.1 SpiralBrain v3.0 — system / code / experiments
Use whenever the system, code, logs, or runs are referenced.
@misc{SpiralBrainV3,
  author = {Cragin, John H.},
  title  = {SpiralBrain v3.0: A Neurosymbolic Agent for Regulatory Intelligence},
  year   = {2026},
  note   = {GitHub repository: \url{https://github.com/jhcragin/SpiralBrain-v3.0-public}}
}
Never attach a DOI or Zenodo publisher to this entry.
________________________________________
4.2 The Regulatory Intelligence Paradigm — theory / framework
Use for definitions, viability-first cognition, H-series framing, and theoretical claims.
@misc{Cragin2026RI,
  author    = {Cragin, John H.},
  title     = {The Regulatory Intelligence Paradigm},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18295507},
  note      = {Preprint, available at \url{https://doi.org/10.5281/zenodo.18295507}}
}
________________________________________
4.3 Synthetic Emotional Calibration (SEC)
Use only when discussing SEC mechanisms, emotional calibration, or integrity regulation.
@misc{Cragin2026Integrity,
  author    = {Cragin, John H.},
  title     = {Synthetic Emotional Calibration SEC},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18370539},
  note      = {Preprint, available at \url{https://doi.org/10.5281/zenodo.18370539}}
}
________________________________________
4.4 Embodied Regulatory Intelligence in Chaotic Physical Systems
Use only when citing Navier–Stokes coupling or embodied physical experiments.
@misc{Cragin2026EmbodiedRI,
  author    = {Cragin, John H.},
  title     = {Embodied Regulatory Intelligence in Chaotic Physical Systems},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18444713},
  note      = {Preprint, available at \url{https://doi.org/10.5281/zenodo.18444713}}
}
________________________________________
4.5 Regulatory Intelligence in Finance
Use only for finance-specific results or claims.
@misc{Cragin2026Finance,
  author    = {Cragin, John H.},
  title     = {Regulatory Intelligence in Finance},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18446550},
  note      = {Preprint, available at \url{https://doi.org/10.5281/zenodo.18446550}}
}
________________________________________
4.6 Emotion as a Control Signal for Symbolic Stability
Use when discussing symbolic stability or control-signal framing.
@misc{Cragin2026EmotionControl,
  author    = {Cragin, John H.},
  title     = {Emotion as a Control Signal for Symbolic Stability},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18446434},
  note      = {Preprint, available at \url{https://doi.org/10.5281/zenodo.18446434}}
}
________________________________________
5. Citation usage rules (lock these)
•	System / code / logs → \cite{SpiralBrainV3}
•	RI theory / definitions → \cite{Cragin2026RI}
•	SEC mechanisms → \cite{Cragin2026Integrity}
•	Embodied / physical systems → \cite{Cragin2026EmbodiedRI}
•	Finance domain → \cite{Cragin2026Finance}
•	Symbolic stability framing → \cite{Cragin2026EmotionControl}
Never mix GitHub and Zenodo identities in one BibTeX entry.
Do not redundantly cite Zenodo papers when the GitHub system is the subject.
________________________________________
6. Author block (canonical)
\author{John H. Cragin \\
Independent Researcher \\
\href{mailto:john.cragin@outlook.com}{john.cragin@outlook.com} \\
ORCID: \href{https://orcid.org/0009-0001-5204-5732}{0009-0001-5204-5732}}
ORCID (when referenced outside the author block):
•	0009-0001-5204-5732
________________________________________
7. Net effect
•	SpiralBrain v3.0 is always defined clearly on first contact.
•	Artifact identity is stable and unambiguous.
•	All references render consistently under plain.
•	Reviewers cannot reasonably ask "what is this?" or "where is it defined?"
This document is now canonical.
If you apply it consistently, you should never have to revisit this again.