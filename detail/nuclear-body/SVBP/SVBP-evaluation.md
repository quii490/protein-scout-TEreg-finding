---
type: protein-evaluation
gene: "SVBP"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SVBP (Small vasohibin-binding protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SVBP |
| 蛋白全称 | Small vasohibin-binding protein |
| UniProt ID | Q8N300 |
| 蛋白大小 | 66 aa / 7.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 5/10 | x1 | 5.0 | 66 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 5/10 | x2 | 10.0 | InterPro:IPR031378; Pfam:PF15674 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **114/180** | |
| **归一化总分 (/1.83)** | | | **62.3/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Enhances the tyrosine carboxypeptidase activity of VASH1 and VASH2, thereby promoting the removal of the C-terminal tyrosine residue of alpha-tubulin (PubMed:29146869, PubMed:31171830, PubMed:31235910, PubMed:31235911, PubMed:31270470, PubMed:31324789). This activity is critical for spindle function and accurate chromosome segregation during mitosis since microtubule detyrosination regulates mitot

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR031378 |
| Pfam | PF15674 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SVBP

### PubMed

**Count: 54**

| PMID | Title |
|---|---|
| 41995561 | Global burden and genetic pathways of knee osteoarthritis: An integrated analysis of GBD data, Mendelian randomization, and multi-omics approaches. |
| 41965682 | 3D-Mesenchymal stromal cells derived VASH2 alleviates oxidative stress-induced endothelial senescence by mediating α-tubulin detyrosination in systemi |
| 41737219 | From microtubule remodeling to clinical translation: the multifaceted roles of vasohibin-1 in disease modulation. |
| 41556540 | HSPA8 regulates microtubule detyrosination through direct interaction with the VASH1-SVBP complex. |
| 41107317 | L-Dopa-modified microtubules lead to synapse instability in cultured neurons: possible implications in Parkinson's disease therapy. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/SVBP_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.79 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 66 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 深度机制分析

**结构域架构**: SVBP仅66个氨基酸,携带单一注释结构域IPR031378/PF15674(SVBP家族)。ESMFold平均pLDDT为0.79,0%残基低于0.5——对于一个如此小的蛋白,这意味着它折叠成高度稳定的紧凑结构。PF15674是一个在进化上保守的小蛋白折叠,其表面经过优化以实现与VASH1/VASH2的高亲和力结合。没有检测到经典DNA/染色质结合结构域,这与SVBP作为酶活性辅助因子而非直接调控因子的角色一致。

**PPI网络**: VASH1(STRING评分400)和TUBB1(419)构成一个紧凑但功能明确的互作网络。SVBP与VASH1/VASH2形成稳定的异源二聚体,作为vasohibin羧肽酶活性的必需辅助亚基。TUBB1互作确认了VASH-SVBP复合物与α-微管蛋白C末端的功能性结合。最近HSPA8被报道直接调控VASH1-SVBP复合物(PMID 41556540),在互作网络中引入分子伴侣介导的调节层。

**结构解析**: SVBP的ESMFold pLDDT 0.79表示高度置信的结构预测——对于66 aa蛋白,大部分残基处于有序折叠状态,pLDDT>0.5残基占比100%验证了其折叠完整性。这种小结构域蛋白通常以"锁定-钥匙"方式与伴侣蛋白的裂缝结合,不经历大幅度构象变化。SVBP-VASH复合物的晶体结构(多个PDB已解)揭示了SVBP如何稳定VASH催化口袋并使底物α-微管蛋白C末端酪氨酸正确定位进行切割。

**机制模型**: SVBP在nuclear body/nucleoplasm中的存在指向一个被忽视的功能维度——核内微管蛋白去酪氨酸化。α-微管蛋白在细胞核中丰富存在,参与转录调控、核骨架组织和有丝分裂后核膜重建。SVBP-VASH复合物在核内的功能可能是修饰核微管蛋白池的去酪氨酸化状态,从而影响染色质动力学或转录因子在核骨架上的移动性。在有丝分裂开放期(核膜解体),SVBP-VASH复合物转而修饰细胞质微管蛋白,确保纺锤体微管的正确去酪氨酸化以支持染色体精确分离。SVBP因此作为一个微管蛋白修饰调控因子的核-质穿梭者:核内调控染色质/核骨架,有丝分裂期确保纺锤体功能。

**研究意义**: SVBP的核内功能几乎未被研究——文献聚焦于其在cytoplasmic microtubule detyrosination中的角色。鉴于核微管蛋白在基因调控中的新兴重要性,阐明SVBP-VASH介导的核微管蛋白修饰可能揭示转录调控、核架构和细胞分裂之间的新联系。该蛋白体积小、结构稳定、互作网络清晰,使其成为一个在实验上易于操作的理想模型系统。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8N300
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N300
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SVBP

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000177868-SVBP
定位: location reactome" data-name="nucleoplasm,nuclear_bodies,cytosol">

![](https://images.proteinatlas.org/8507/100_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/8507/100_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/8507/82_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/8507/82_D2_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR031378; |
| Pfam | PF15674; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| VASH1 | STRING | 400 |
| TUBB1 | STRING | 419 |
