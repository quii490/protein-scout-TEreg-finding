---
type: protein-evaluation
gene: "ARMC8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARMC8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARMC8 / 无 |
| 蛋白名称 | Armadillo repeat-containing protein 8 |
| 蛋白大小 | 673 aa / 75.5 kDa |
| UniProt ID | Q8IUR7 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 02:32:34 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, C... |
| 蛋白大小 | 10/10 | x1 | 10 | 673 aa / 75.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=23 篇 (21-40->8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=94.1; PDB: 7NSC |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 4; Pfam: 1; IPR011989, IPR016024... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **162.0/180** | |
| **归一化总分 (/1.83)** | | | **88.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Vesicles, Cytosol | Supported |
| UniProt | Nucleus, Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- GID complex (GO:0034657)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- specific granule lumen (GO:0035580)
- tertiary granule lumen (GO:1904724)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 673 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 37 |

**关键文献**:
1. The GID ubiquitin ligase complex is a regulator of AMPK activity and organismal lifespan.. *Autophagy*. PMID: 31795790
2. The micro RNA hsa-miR-377-3p inhibits tumor growth in malignant melanoma.. *RSC advances*. PMID: 35516861
3. The interactome of tau phosphorylated at T217 in Alzheimer's disease human brain tissue.. *Acta neuropathologica*. PMID: 40317322
4. Armc8 is an evolutionarily conserved armadillo protein involved in cell-cell adhesion complexes through multiple molecular interactions.. *Bioscience reports*. PMID: 30482882
5. ARMc8 indicates aggressive colon cancers and promotes invasiveness and migration of colon cancer cells.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 26081621

**评价**: 较高新颖性，研究尚处早期阶段（PubMed 21-40篇）。新颖性评分 8/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 92.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 96.0% |
| 可用 PDB 条目 | 7NSC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=94.1），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR038739; Pfam: PF00514 |

**染色质调控潜力分析**: 存在 5 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YPEL5 | 0.921 | 0.767 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RNPS1 | anti bait coimmunoprecipitation | pubmed:17353931 |
| CHM | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| CUL3 | tandem affinity purification | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2010.11.017 |
| RMND5A | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| GDNF | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SFRP2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| TLE4 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| Pde4dip | anti bait coimmunoprecipitation | pubmed:28671696|doi:10.1038/nn.4594|imex:IM-26285 |
| GCH1 | pull down | pubmed:30833792|imex:IM-26691 |
| ESR1 | tandem affinity purification | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 7NSC | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 88.5/100

**核心优势**:
1. ARMC8 -- Armadillo repeat-containing protein 8，较高新颖性，研究尚处早期阶段。
2. 蛋白大小673 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold高质量预测（pLDDT=94.1），结构可信度高。
4. 已有PDB实验结构：7NSC。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8IUR7
- Protein Atlas: https://www.proteinatlas.org/search/ARMC8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARMC8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUR7
- STRING: https://string-db.org/network/9606.ARMC8
- Packet data timestamp: 2026-06-03 02:32:34

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000114098-ARMC8/subcellular

![](https://images.proteinatlas.org/44869/1050_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/44869/1050_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/44869/698_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/44869/698_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/44869/859_H2_3_red_green.jpg)
![](https://images.proteinatlas.org/44869/859_H2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IUR7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
