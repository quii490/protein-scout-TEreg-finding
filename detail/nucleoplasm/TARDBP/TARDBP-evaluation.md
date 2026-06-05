---
type: protein-evaluation
gene: "TARDBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TARDBP — REJECTED (研究热度过高 (PubMed strict=704，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TARDBP / TDP43 |
| 蛋白名称 | TAR DNA-binding protein 43 |
| 蛋白大小 | 414 aa / 44.7 kDa |
| UniProt ID | Q13148 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasm, Stress granule; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 414 aa / 44.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=704 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 1WF0, 2CQG, 2N2C, 2N3X, 2N4G, 2N4H, 2N4P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR000504, IPR049124, IPR041 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, Stress granule; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasmic stress granule (GO:0010494)
- interchromatin granule (GO:0035061)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perichromatin fibrils (GO:0005726)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 704 |
| PubMed broad count | 2477 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TDP43 |

**关键文献**:
1. The genetics of amyotrophic lateral sclerosis.. *Current opinion in neurology*. PMID: 38967083
2. TDP-43 Pathology in Alzheimer's Disease.. *Molecular neurodegeneration*. PMID: 34930382
3. PIKFYVE inhibition mitigates disease in models of diverse forms of ALS.. *Cell*. PMID: 36754049
4. ALS Genetics: Gains, Losses, and Implications for Future Therapies.. *Neuron*. PMID: 32931756
5. TDP-43 proteinopathies: a new wave of neurodegenerative diseases.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 33177049

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.7% |
| 置信残基 (pLDDT 70-90) 占比 | 51.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 37.7% |
| 有序区域 (pLDDT>70) 占比 | 52.4% |
| 可用 PDB 条目 | 1WF0, 2CQG, 2N2C, 2N3X, 2N4G, 2N4H, 2N4P, 4BS2, 4IUF, 4Y00 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 52.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR000504, IPR049124, IPR041105; Pfam: PF00076, PF20910, PF18694 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000081142.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| XRN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ZHX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NSFL1C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 1WF0, 2CQG, 2N2C, 2N3X, 2N4G,  | pLDDT=65.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, Stress granule; Mit / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TARDBP — TAR DNA-binding protein 43，研究基础较多，新颖性有限。
2. 蛋白大小414 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 704 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 704 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13148
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120948-TARDBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TARDBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13148
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000120948-TARDBP/subcellular

![](https://images.proteinatlas.org/17284/138_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/17284/138_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/17284/139_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/17284/139_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/17284/166_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/17284/166_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13148-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
