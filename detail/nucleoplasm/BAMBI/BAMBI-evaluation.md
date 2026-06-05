---
type: protein-evaluation
gene: "BAMBI"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BAMBI — REJECTED (研究热度过高 (PubMed strict=226，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BAMBI / NMA |
| 蛋白名称 | BMP and activin membrane-bound inhibitor homolog |
| 蛋白大小 | 260 aa / 29.1 kDa |
| UniProt ID | Q13145 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoli fibrillar center, Lipid droplets; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 260 aa / 29.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=226 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009345, IPR045806, IPR045807, IPR045860; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.0/180** | |
| **归一化总分** | | | **37.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoli fibrillar center, Lipid droplets | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 226 |
| PubMed broad count | 704 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NMA |

**关键文献**:
1. Multi‑layered prevention and treatment of chronic inflammation, organ fibrosis and cancer associated with canonical WNT/β‑catenin signaling activation (Review).. *International journal of molecular medicine*. PMID: 29786110
2. Hypoxia-responsive PPARGC1A/BAMBI/ACSL5 axis promotes progression and resistance to lenvatinib in hepatocellular carcinoma.. *Oncogene*. PMID: 36932115
3. miR-20a: a key regulator of orthodontic tooth movement via BMP2 signaling pathway modulation.. *Connective tissue research*. PMID: 38922815
4. BMP and activin receptor membrane bound inhibitor: BAMBI has multiple roles in gene expression and diseases (Review).. *Experimental and therapeutic medicine*. PMID: 38125356
5. Competing roles of TGFbeta and Nma/BAMBI in odontoblasts.. *Journal of dental research*. PMID: 20173182

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 4.2% |
| 置信残基 (pLDDT 70-90) 占比 | 41.9% |
| 中等置信 (pLDDT 50-70) 占比 | 24.6% |
| 低置信 (pLDDT<50) 占比 | 29.2% |
| 有序区域 (pLDDT>70) 占比 | 46.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 46.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009345, IPR045806, IPR045807, IPR045860; Pfam: PF06211, PF19337 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TGFBR1 | 0.988 | 0.292 | — |
| SMAD7 | 0.977 | 0.292 | — |
| ACVR1 | 0.972 | 0.292 | — |
| FZD5 | 0.965 | 0.292 | — |
| LRP6 | 0.963 | 0.292 | — |
| BMPR1A | 0.956 | 0.292 | — |
| BMPR1B | 0.954 | 0.292 | — |
| DVL2 | 0.934 | 0.292 | — |
| FZD4 | 0.924 | 0.000 | — |
| FZD9 | 0.922 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOX30 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NKG7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| Q80BV4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| ENST00000375533 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Vesicles; 额外: Nucleoli fibrillar center, Lipid dro | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BAMBI — BMP and activin membrane-bound inhibitor homolog，研究基础较多，新颖性有限。
2. 蛋白大小260 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 226 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 226 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13145
- Protein Atlas: https://www.proteinatlas.org/ENSG00000095739-BAMBI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BAMBI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13145
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000095739-BAMBI/subcellular

![](https://images.proteinatlas.org/10819/1601_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10819/1601_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/10819/1682_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10819/1682_D3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/10819/1732_H2_18_cr58060cebb51f0_blue_red_green.jpg)
![](https://images.proteinatlas.org/10819/1732_H2_28_cr58060cf53d8d7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13145-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
