---
type: protein-evaluation
gene: "PKP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PKP1 — REJECTED (研究热度过高 (PubMed strict=118，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PKP1 |
| 蛋白名称 | Plakophilin-1 |
| 蛋白大小 | 747 aa / 82.9 kDa |
| UniProt ID | Q13835 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cell junction, desmosome; Nucleus; Nucleus; Cytoplasm, perin |
| 蛋白大小 | 10/10 | ×1 | 10 | 747 aa / 82.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=118 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.0; PDB: 1XM9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Cell junction, desmosome; Nucleus; Nucleus; Cytoplasm, perinuclear region; Cytoplasm; Cell junction,... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- desmosome (GO:0030057)
- ficolin-1-rich granule membrane (GO:0101003)
- intermediate filament (GO:0005882)
- nuclear stress granule (GO:0097165)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 118 |
| PubMed broad count | 179 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Plakophilin 1 in carcinogenesis.. *Molecular carcinogenesis*. PMID: 38888207
2. Ectodermal dysplasia-skin fragility syndrome.. *Dermatologic clinics*. PMID: 19945625
3. PKP1 and MYC create a feedforward loop linking transcription and translation in squamous cell lung cancer.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 35182388
4. Multi-omics analysis unveils a four-gene prognostic signature in esophageal squamous carcinoma and the therapeutic potential of PKP1.. *BMC cancer*. PMID: 40281492
5. Plakophilin 1 enhances MYC translation, promoting squamous cell lung cancer.. *Oncogene*. PMID: 31822797

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.0 |
| 高置信度残基 (pLDDT>90) 占比 | 41.2% |
| 置信残基 (pLDDT 70-90) 占比 | 16.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 57.8% |
| 可用 PDB 条目 | 1XM9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.0），有序残基占 57.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam: PF00514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DSP | 0.995 | 0.548 | — |
| DSG1 | 0.994 | 0.663 | — |
| DSG3 | 0.951 | 0.134 | — |
| JUP | 0.946 | 0.098 | — |
| PKP3 | 0.916 | 0.000 | — |
| DSC1 | 0.905 | 0.543 | — |
| DSG2 | 0.895 | 0.134 | — |
| DSC3 | 0.894 | 0.134 | — |
| EVPL | 0.890 | 0.045 | — |
| PPL | 0.866 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nphp4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Mks1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| PBL35 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| EIF3G1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| WRKY7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| Q93ZY0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| PBL15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| EBI-4424518 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| WIPI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.0 + PDB: 1XM9 | pLDDT=69.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell junction, desmosome; Nucleus; Nucleus; Cytopl / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PKP1 — Plakophilin-1，研究基础较多，新颖性有限。
2. 蛋白大小747 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 118 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 118 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13835
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081277-PKP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PKP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13835
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000081277-PKP1/subcellular

![](https://images.proteinatlas.org/27221/1033_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/27221/1033_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/27221/254_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/27221/254_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/27221/291_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/27221/291_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13835-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
