---
type: gene-evaluation
gene: ACSF3
date: 2026-06-28
tags: [rejected, mitochondrial, fatty-acid-synthesis, malonate-CoA-ligase]
status: rejected
---

# ACSF3 - Rejection Report

## Rejection Summary

**Gene:** ACSF3
**Protein:** Malonate--CoA ligase ACSF3, mitochondrial
**UniProt:** Q4G176

**Reason for rejection:** ACSF3 is a mitochondrial enzyme that catalyzes the initial step of intramitochondrial fatty acid synthesis by activating malonate and methylmalonate into their CoA thioesters. Its GO-CC annotations are exclusively mitochondrial: mitochondrial matrix and mitochondrion. UniProt lists its sole subcellular location as "Mitochondrion." There is no nuclear GO-CC term and no evidence of nuclear localization or function. This is a dedicated mitochondrial metabolic enzyme with no connection to nuclear biology or TE regulation.

### 深度机制分析

**结构域架构**：ACSF3（Q4G176, Malonate--CoA ligase ACSF3, mitochondrial）属于acyl-CoA synthetase（ACS）家族，含conserved ATP/AMP-binding domain和acyl-CoA synthetase catalytic domain。该酶催化malonate + CoA + ATP→malonyl-CoA + AMP + PPi的两步反应——第一步ATP-dependent adenylation of malonate carboxylate group→malonyl-AMP intermediate——第二步thioesterification with CoA-SH→malonyl-CoA。Malonyl-CoA是mitochondrial fatty acid synthesis（mtFAS）的building block——mtFAS pathway产生octanoyl-ACP——作为lipoic acid synthesis和mitochondrial tRNA modification的前体。

**PPI互作网络解读**：ACSF3为mitochondrial matrix enzyme——PPI限定于mitochondrial metabolic network——关键functional partners包括MCAT（malonyl-CoA-acyl carrier protein acyltransferase, mtFAS第二步酶）、OXSM（3-oxoacyl-ACP synthase, mtFAS第三步酶）和MECR（mitochondrial enoyl-ACP reductase, mtFAS末端酶）。这些酶共同构成mtFAS pathway——ACSF3的knockout导致severe metabolic disorder（combined malonic and methylmalonic aciduria, OMIM #614265）。

**结构解读**：ACSF3的AlphaFold预测结构（pLDDT未显式标注）显示conserved two-domain ACS fold——N-terminal large domain（~500 aa）含ATP-binding Rossmann fold——C-terminal small domain（~100 aa）含CoA-binding site。Active site cleft位于domain interface——交替open（substrate loading）和closed（adenylation/transfer）conformation——domain rotation ~140 degree during catalytic cycle。ACSF3特异性识别malonate和methylmalonate（drawn from cytoplasmic malonate pool via mitochondrial malonate transporter）——利用ATP能量形成high-energy thioester bond——用于下游mtFAS condensation。

**机制模型**：ACSF3-mtFAS pathway在mitochondrial metabolism中执行three critical functions：（1）Lipoic acid synthesis——mtFAS-derived octanoyl-ACP转移至glycine cleavage system H protein（GCSH）——形成lipoyl-GCSH——作为PDH（pyruvate dehydrogenase）、KGDH（alpha-ketoglutarate dehydrogenase）和BCKDH（branched-chain ketoacid dehydrogenase）的essential cofactor；（2）Mitochondrial tRNA modification——mtFAS产物修饰mt-tRNA(Lys)和mt-tRNA(Glu)的uridine base——影响mitochondrial translation fidelity；（3）Mitochondrial respiratory chain assembly——mtFAS中间体可能参与Fe-S cluster biosynthesis和ETC complex assembly。

**TE调控展望**：ACSF3作为dedicated mitochondrial enzyme，与TE调控缺乏直接连接。然而mitochondrial metabolism通过以下间接途径可能影响nuclear epigenetic landscape：（1）Mitochondrial one-carbon metabolism（folate cycle）产生S-adenosylmethionine（SAM）——universal methyl donor——mtFAS dysfunction可能扰乱mitochondrial one-carbon flux→改变cytosolic/nuclear SAM pool→影响DNA and histone methylation——包括TE区域的CpG methylation和H3K9me3；（2）Mitochondrial TCA cycle metabolites（alpha-ketoglutarate, succinate, fumarate）作为TET（DNA demethylase）和JmjC-domain histone demethylase的cofactor或inhibitor——ACSF3 deficiency可能导致TCA cycle intermediate accumulation→inhibit TET/JmjC activity→hyper-methylation of TE regions；（3）Mitochondrial stress signaling（mtUPR, ISR）通过ATF4/CHOP transcription program→调控chromatin state——可能影响TE activation。建议在ACSF3 mutation/knockout的metabolomics和epigenomics data中检测TE methylation和expression水平。
