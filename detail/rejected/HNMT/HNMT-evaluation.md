---
type: protein-evaluation
gene: "HNMT"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: rejected
---

## HNMT 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HNMT |
| UniProt ID | P50135 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | — | ×4 | — | — |
| 📏 蛋白大小 | — | ×1 | — | — |
| 🆕 研究新颖性 | 0 | ×5 | 0 | PubMed 191 篇 >100 → 淘汰 |
| 🏗️ 三维结构 | — | ×3 | — | — |
| 🧬 调控结构域 | — | ×2 | — | — |
| 🔗 PPI 网络 | — | ×3 | — | — |
| ➕ 互证加分 | — | max +3 | — | — |
| **原始总分** | | | **淘汰** | |
| **归一化总分** | | | **淘汰** | |

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 淘汰原因

**PubMed 总数: 191 篇 > 100 篇 → 一票否决。**

根据评分规则，PubMed >100 篇的蛋白直接淘汰。HNMT 已有 191 篇文献，研究过于拥挤，不符合"寻找新颖核蛋白"的核心目标。

### 深度机制分析

**结构域架构**：HNMT（P50135, Histamine N-methyltransferase, 292 aa, 33 kDa）是S-adenosyl-L-methionine（SAM）-dependent methyltransferase——催化histamine的N-methylation→产生N(tau)-methylhistamine。结构域：SAM-dependent methyltransferase domain（Pfam PF01234, InterPro IPR016673）——典型Rossmann fold（alpha/beta sandwich）——中央6-stranded parallel beta-sheet夹于alpha-helices之间——SAM cofactor结合于Rossmann fold C-terminus——histamine substrate进入active site cleft——His142（general base）deprotonate histamine imidazole nitrogen——触发nucleophilic attack on SAM methyl group→SN2-type methyl transfer→S-adenosyl-L-homocysteine（SAH）作为byproduct产生。HNMT与HNMT（N-terminal domain）和HNMT_C（C-terminal domain）构成compact single-domain globular fold——无extended IDR regions。

**PPI互作网络解读**：HNMT作为metabolic enzyme——PPI network偏功能性代谢而非regulatory hub——STRING中与ABP1（amiloride binding protein 1, diamine oxidase）形成histamine degradation pathway——ABP1催化histamine的oxidative deamination——HNMT催化histamine的N-methylation——两者构成cellular histamine clearance的两个parallel pathways。HNMT也与COMT（catechol O-methyltransferase, SAM-dependent methyltransferase family）存在functional similarity——两者均为SAM-dependent small molecule methyltransferase。

**结构解读**：PDB实验结构已解析（如PDB: 1JQE, 2AOT）——HNMT的结构揭示narrow active site tunnel（~10 angstrom deep）——仅accommodate histamine-sized substrates——不能accommodate bulkier biogenic amines（如acetylcholine, serotonin）——解释了HNMT的高度substrate specificity。Key catalytic residues: His142（general base）、Glu28（SAM carboxylate coordination）、Tyr147（transition state stabilization via pi-stacking）。HNMT的inhibitor结合模式（如amodiaquine, quinacrine, metoprine）已由多个共晶结构阐明——这些抗疟药巧合地inhibit HNMT——导致histamine积累。

**机制模型**：（1）Histamine inactivation——HNMT主要在CNS（brain）和airway epithelium中表达——将histamine转化为biologically inactive N(tau)-methylhistamine——终止histamine-mediated signaling（histamine H1/H2/H3/H4 receptor activation的终止）。（2）SAM consumption——HNMT催化每个methyl transfer消耗一个SAM molecule→产生SAH——SAH是所有SAM-dependent methyltransferase（包括DNA methyltransferase DNMT1/3A/3B和histone methyltransferase）的potent feedback inhibitor——HNMT活性升高→SAH accumulation→global inhibition of methylation reactions→可能indirectly affect TE methylation landscape。（3）Disease association——HNMT polymorphism（Thr105Ile, rs11558538）降低enzyme activity——与asthma, allergic rhinitis, and atopic dermatitis相关。

**TE调控展望**：HNMT通过SAM/SAH metabolism间接链接到TE epigenetic regulation。HNMT是cellular SAM consumer之一——与其他SAM-dependent methyltransferase（DNMT, histone methyltransferase）competition for limited SAM pool——HNMT overexpression可能导致SAM depletion→reduced DNA/histone methylation→potential TE de-repression。Conversely, HNMT-derived SAH product accumulation→feedback inhibition of DNMTs and HMTs→affect TE methylation maintenance。SAM/SAH ratio（methylation index）是global methylation capacity的关键indicator——HNMT activity作为methylation sink可能significantly影响此ratio。但这些均为间接metabolic connection——HNMT自身不结合DNA/chromatin也不target TE——无direct TE recognition or regulation capability。研究热度极高（PubMed=191）进一步降低了其作为discovery target的价值——优先探索chromatin-bound SAM-dependent methyltransferases with direct TE association。

### 4. 数据来源
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22HNMT%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprotkb/P50135 (if available)

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000150540-HNMT/subcellular

![](https://images.proteinatlas.org/73754/1763_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/73754/1763_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/73754/1765_B7_3_red_green.jpg)
![](https://images.proteinatlas.org/73754/1765_B7_4_red_green.jpg)
![](https://images.proteinatlas.org/73754/1823_B11_33_red_green.jpg)
![](https://images.proteinatlas.org/73754/1823_B11_34_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
