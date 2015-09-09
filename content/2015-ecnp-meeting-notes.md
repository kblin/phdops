Title: ECNP 2015 Meeting Notes
Date: 2015-09-09 13:13
Category: Science
Tags: ecnp, conference, natural products
Slug: 2015-ecnp-meeting-notes
Author: Kai Blin
Summary: Notes from the 2nd European Conference for Natural Products

My personal notes from the 2nd European Conference for Natural Products.

##Monday

###Manuela Toisin: Chemical probes for the capture and functionalisation of polyketide intermediates

"Stealing" intermediates with non-hydrolysable ACP mimics. This works in vivo
and in vitro. Capture can be combined with functional groups on the probes to
then do downstream "click" chemistry or similar modifications to generate new
motifs.

###Martin Grininger: Engineering FAS for directed polyketide synthesis

Using the close relationship of PKSs & FASs to utilise the insights on FAS
pathways. Work on chain length control for iterative FASs & PKSs. Built up
kinetic models. Chain length control seems to depend on binding affinity to AT
(elongation happens) or MPT (exit of iteration happens) domains.

###Florian Seebeck: Mechanisms of ergothioneine biosynthesis

Ergothioneine, a thiohistidine produced by bacteria and some fungi. Uptake
transporters in all eukaryotes, though. Might be an antioxidant, as
ergothioneine-transport-defective nematodes show oxidative DNA damage.
Ergothioneine also occurs in some secondary metabolite products.
Ovothiol is a similar thiohistidine. _Erwinia tasmaniensis_ uses ovothiol to
protect itself from the H<sub>2</sub>O<sub>2</sub> oxidative burst during plant infection.
EgtD is a histidine methyltransferase that, despite similar catalytic efficiency
per step, prefers to methylate histidine all the way to 3-methyl-histidine.
Me-His and especially 2-Me-His have a much higher affinity to active site, and
thus prevent the exessive methylation of all histidine in the cell. Also,
3-Me-His has a higher affinity to the active site than His, thus serving as
feedback inhibitor.
EgtB is a 3-His facial triade non-heme iron enzyme that synthesises sulfoxide
moieties in a 4 electron oxidation, a very unique mode of action. Conservative
mutation can convert EgtB into a deoxidase, raising questions about current
conceptions of how deoxidases work.

###Tobias Gulder: Novel (Bio-)synthetic Strategies to Polycyclic Natural Products

Talking about polycyclic tetramate macrolactams (PTMs). Very unusual iterative
PKS/NRPS module? Multiple reductive tailoring enzymes perform a hydride induced
cyclisation cascade. Heterologously expressed enzymes can perform the synthesis
in vitro with a similar yield as full synthesis, but with simpler experimental
setup.

###Markus Nett: Biosynthetic pathways from predatory bacteria

_Pyxidicoccus fallax_ produces RNA synthesis inhibiting macrolide antibiotic,
apparently very specific against Gram+ive prey.

_Herpetosiphon aurantiacus_, a filamentous predatory bacterium. Contains many
secondary metabolites. Most gene clusters are cryptic, though, and no genetic
tools exist.

###Daniel Petras: The biosynthesis of albicidins

Albicidin is a PKS-NRPS hybrid gyrase inhibitor. Contains a large number of
unusual AAs. Used Pieter Dorrestein's clustering tool (GNPS) to analyse
LC-MS/MS data.

###Martin Schäfer: Structure-function relationships of the DNA gyrase inhibitor simocyclinone

Aminocoumarin cluster in _Streptomyces antibioticus_ Tü6040. Is there a sequence
for Tü6040 available? ~72 kb cluster. Literature pathway for Simocyclinone D8 is
likely wrong, SimC7, while important for antibiotic activity of the product,
seems to be a ketoreductase, not a dehydratase.

###Roderich Süssmuth: Peptide Antibiotics

Honeybees are important for cross-pollination, and thus important for
agriculture. _Paenibacillus larvae_ is a highly successful bee larvae pathogen.
_P. larvae_ genome encodes for 4 NRPS clusters. Paenilamicin, an 11-monomer
modular PKS/NRPS hybrid, has some antibacterial & antifungal activity.

Engineering on the cyclodepsipeptides like enniatins show that substrate
specificity & chain length control is dependent on specific modules in the
iterative NRPS cluster.

###Xinyu Liu: Hapalindole alkaloid biosynthesis: a treasure trove of novel enzymatic transformations

Stignematalean cyanobacteria, large regiochemical diversity in a single producer
organism. Identification of two representative gene clusters gives insights into
biosynthesis.  Identified a new type of halogenases, the carrier protein
dependent NHI halogenases. Both narrow & broad spectrum halogenases were
identified. Enzymes are evolvable, interesting for synthetic biology.

###Tohru Dairi: A novel enzyme capping N-terminus of various peptides with amidino-PheGly derivatives

Pheganomycin biosynthesis incooperates a non-proteinogenic N-terminus and a very
variable C-terminus. So both ribosomal and NRPS synthesis would not be able to
produce this compound. Enzymes for the production of the precursor
dihydro-phenylglycine were found. Also, a RiPP prepeptide ORF and a peptidase
were found. But how are these compounds linked? Cluster seems to contain an NRPS
domain (antiSMASH predicts Valin specificity), but a knockout shows no
pheganomycin deficiency. Instead, a peptide ligase was observed. The peptide
ligase needs an amidino group on the N-terminal substrate, and can accept a wide
variety of C-terminal peptides. Crystal structure analysis shows a large binding
pocket and a long cleft around the catalytic Arg residue.

###Kenan Bozhüyük & Florian Fleischhacker: Reprogramming nonribosomal peptide synthetases from _Xenorhabdus_ and _Photorhabdus_.

Exchange ATC units, not TCA modules. C-A linker region highly conserved, cut
before `WNATE` motif to combine units. Less yield loss compared to module
exchange.

###Till Schäberle: Corallopyronin A - two in one sweep

Observed new kind of shift domain, similar to DH domain but with different
residues in the active site.

##Tuesday:

###Keynote: David Sherman

Polyketide synthetases are modular systems, but despite all the hype,
lego-isation of PKSs has not been viable so far. On the way to a better
understanding of the biosynthesis, chemoenzymatic synthesis helped to work with
individual modules.
Cryo-EM, and individual PKS/NRPS modules are at the lower end of the size you
can visualise with that, is also giving great new insights in the mode of
action. PikAIII, different to the excised DEBS-KS-AT model, has a single
reaction center in the dimer.
Substrate controlled divergence seems to direkt the chain length in methymycin /
pikromycin biosysnthesis.
The pikromycin TE can be engineered to allow for unnatural products with
different stereochemistry by a single AA replacement in the active site. Reasons
still not known.

###Christian Ducho: Structure-activity relationship studies on muraymycin nucleoside-peptide antibiotics

Full synthesis of Muramycin-related structures allows to play with a number of
side-chains to find new inhibitors to membrane protein translocase MraY. Assay
is _in vitro_, though, not convinced that bioavailability is given.
An omega-functionalised fatty acid was proposed to help get the substance
through lipid membranes. To check, a flouresescence-tagged version of the
omega-functionalised fatty acid was combined with immobilised vesicles and
seemed to penetrate the membrane of those vesicles. Still, not entirely
convinced. There's a reason why nature targes cell wall biosynthesis pathways
outside of the membrane, not inside.

###Esther Schmitt: Cyclomarin A Kills Mycobacteria and Malaria Parasites Using Distinct Modes of Action

Malarial parasites _Plasmodium vivax_ and _Plasmodium falciparum_ have a complex
life cycle. Most malarial drugs attack plasmodia in the blood stages, where they
are easily accessible. This works well against _P. falciparum_, but not as well
agains the "relapsing malaria" caused by _P. vivax_, where some parasites go
dormant inside liver cells, only to resurface at some later point, often years
later. Additionaly, the current gold standard treatment of Arteminisin, while
having been used successfully > 800 Mio. times already, is beginning to fail in
some tropical regions with plasmodia beginning to show resistance due to a point
mutation.

Cyclomarin A works against Mycobacteria by deregulating the ClpC1 protease, thus
also killing of dormant mycobacteria once they leave hibernation. While
plasmodia have a Clp protease analog, the target of Cyclomarin A is the
diadenosine triphosphate hydrolase PFAp3Ase. PFAp3Ase cleaves the signaling
molecule Ap3A, which in turn seems to be a tumor suppressor in mammals. Function
in plasmodia is unknown.

Challenge on investigating the dormant stage is that experiments need to be done
in monkey primary hepatocytes, which only survive in cell culture for several
days. On the other hand, forming dormant stages by the monkey-specific _P.
cynomolgi_ also takes several days, race against time.

###Mark Brönstrup: Structure-based optimisation of anabaenopeptins as TAFI inhibitors

Pilot stody to explore NPs from cyanobacteria. Anabaenopeptin B is a good TAFI
inhibitor, thus functioning as an antithromboical agent. However, a generic
Astra Zeneca patent covers the function, without being anabaenopeptin-specific.
Also, the oral bioavailability is not really good. Idea: generate analogs with
better bioavailability not covered by patent. Crystal structure of TAFI with
bound anabaenopeptin B gave insights into the mode of action, allowing to create
simple but active derivatives.
While current leads are based on full synthesis, the functional insights from
the natural product was vital to the understanding the bioactivity.

###Shu-Ming Li: Prenyltransferase genes in fungal genomes

Prenylated indole alkaloids in fungy are (di)peptide derivatives with prenyl
moiety at different positions, and with different biological activities. The
corresponding prenyltransferases cluster into different classes in a
phylogenetic analysis.

Prenylation of the indole ring incresases the cytotoxicity of cyclic dipeptides.

###Jennifer Herrmann: Antibacterial disciformycins from myxobacteria as novel RNA polymerase inhibitors

Disciformicins inhibit _S. aureus_ RNA polymerase subunits RpoB and RpoC, and
show no cross-resistance to other known RNA polymerase inhibitors.

###Peter Spieth: New strategies to bypass plant-based bioinsecticide production

The Neem tree (_Azadirachta indica_) contains endophytes that seems to produce a
wide variety of compounds with insecticidal activity.

## Wednesday

###Tilmann Weber: Tools for the genomics driven discovery and engineering of natural products

antiSMASH talk! Tilmann is not only talking about antiSMASH, but also presenting
the class IV lanthipeptide work on streptocollin, and our CRISPR-Cas9 toolset.

###Olga Genilloud: Accessing previously uncultured bacteria with the Diffusion Sandwich System

Goal: Access as of yet uncultured bacteria to find new natural products.
Reformulated culturing media, supplements of signalling molecules, diffusion
chamber systems.

Diffusion Sandwich Systems are simpler to build than iChip. Basically a metal
plate with holes. Holes contain plugs of agar or rubber gum containing 1-10
viable cells. Then buried in soil for 1-3 months. Growing cells are then
"domesticated", Pilot study increased culturability of viable cells from 0.06%
using the standard dilution approach up to ~8% using the sandwich system.

###Chambers Hughes: Reactivity-guided isolation of biologically-active natural products

Ideally, you want to identify irreversible inhibitors of targets, substances
that covalently bind their targets. But screening for this by target or
biosynthesis is hard, as they are very diverse. However, they are often
electrophilic, and that can be used for the screening. Use Thiol-based probes to
scan for this, that contains a nice UV tag, a Br tag for MS, and a
stereochemical reference. Alternative probe with a Cl tag and UV tag works very
specifically on epoxide-containing products.

###Max Crüsemann: Novel secondary metabolites from Salinispora through mass spectrometry-guidede genome mining approaches

We're drowning in genomic data, and methods to bridge MS data to genomic data is
desirable. Pieter Dorrestein's Global natural products social (GNPS) molecular
networking.

###Wilfried Schwab: Activity-based profiling of physiologic aglycone library

Natural products from plants seem to be annoying to deal with.
