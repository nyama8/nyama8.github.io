---
# Fields: title, order (position on the Research page),
#         image (figure on the topic page, also used on the card), alt (short description of it),
#         thumbnail (optional: a different, e.g. cropped, picture for the card),
#         summary (2–3 sentences for the card), papers (ids from _data/publications.yml).
# The text below the --- line is the topic's own page.
title: Quantum transduction
order: 1
image: /assets/img/research/transduction.png
thumbnail: /assets/img/research/transduction-thumb.jpg
alt: >-
  Diagram of two dilution refrigerators, each with a quantum processor (QPU) and a
  microwave-to-optical (M2O) transducer, connected by a room-temperature fiber-optic link.
summary: >-
  Novel devices with enhanced nonlinearities for microwave-optical quantum frequency transduction.
# Highlights (optional): papers shown above "Related papers" and left out of that list.
#   id: paper id; text: a few sentences in your words;
#   image, alt, caption: optional figure (check the journal's reuse policy; credit it in the caption)
highlights:
  - id: yama2026transduction
    text: >-
      In this work we develop <b>a new electro-optic (EO) transduction platform</b> that utilizes the strong nonlinearity of quantum-well (QW) exciton polaritons.
      Excitons (electron-hole pairs bound by the Coulomb interaction) formed in QW heterostructures exhibit strong EO nonlinearities via the quantum-confined Stark effect.
      Strong coupling of excitons and optical photons results in <b>exciton polaritons</b> — quasi-particles that inherit the properties of both light and matter.
      We show that the effective nonlinear coupling strength of the exciton polaritons can be up to <b>five orders of magnitude larger than traditional bulk EO nonlinearities</b>, enabling simultaneously efficient, low-noise, and wide-bandwidth transduction <b>with microwatt pump powers and modest quality factors</b>.
    image: /assets/img/research/transduction-highlight.png
    alt: >-
      Five-panel overview figure: (a) circuit diagram of an optical cavity containing a
      chi-2 medium coupled to a microwave LC circuit, with a frequency diagram;
      (b) GaAs/AlGaAs quantum-well band diagrams with and without a bias field;
      (c) polariton frequencies versus bias field; (d) refractive index and extinction
      versus detuning; (e) magnitude of chi-2 versus detuning compared with BaTiO3 and LiNbO3.
    caption: >-
      (a) A typical EO transduction device with a χ⁽²⁾ medium within an optical cavity and an LC
      circuit. (b) GaAs/AlGaAs quantum-well wavefunctions. (c) Upper and lower polariton (UP, LP)
      frequencies versus bias field. (d) Semiclassical index n and extinction k near the exciton
      resonance. (e) |χ⁽²⁾| versus detuning, compared with BaTiO₃ and LiNbO₃.
papers: [yama2026transduction, chen2025sciadv]
---

Superconducting quantum systems need to operate at millikelvin temperatures where thermal noise at their microwave operation frequencies is suppressed.
This poses a significant barrier to scaling as state-of-the-art cryogenic systems (dilution refrigerators) have limited cooling capacity.
This problem is exacerbated by the fact that each qubit typically needs 1--3 dedicated dc/microwave lines for tuning, readout, and control, which all increase the heat load and complexity of scaling in what is known as the I/O bottleneck.
One solution is to utilize modular architectures wherein different processor chips, each in their own dilution refrigerator, are connected via low-loss microwave links.
However, this is practically challenging as the microwave links need to also be maintained at millikelvin temperatures which adds an additional thermal load and limits the practical physical length scale of the connection.

A desirable alternative is to establish fiber-optic links which operate at optical frequencies.
This requires an element, a microwave-optical quantum transducer, which can coherently and faithfully convert microwave quantum signals to optical frequencies.
Given such a transducer, one could utilize the large optical bandwidths to replace multiple microwave control lines with a single, low-thermal-conductivity optical fiber which alleviates the I/O bottleneck.
These optical fiber links are essentially free of thermal noise even at room temperature, and can transmit quantum signals over long distances with low loss.

However, microwave-optical quantum transduction with simultaneously high efficiency, low noise, and wide bandwidth has not yet been achieved.
The main reason for this is that the transduction process relies on optical nonlinearities which are intrinsically weak.
Traditional approaches using electro-optic or electro-optomechanical interactions have required high-quality factor resonators (which limit bandwidth) and large pump powers (which inject noise through heating) to be efficient.

My research seeks to find ways of addressing this problem fundamentally by increasing the strength of the nonlinearity to relax the quality factor and pump requirements.
