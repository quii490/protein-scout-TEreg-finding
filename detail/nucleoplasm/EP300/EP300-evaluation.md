---
type: protein-evaluation
gene: "EP300"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EP300 — REJECTED (研究热度过高 (PubMed strict=994，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EP300 / P300 |
| 蛋白名称 | Histone acetyltransferase p300 |
| 蛋白大小 | 2414 aa / 264.2 kDa |
| UniProt ID | Q09472 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome, Cytosol; UniProt: Cytoplasm; Nucleus; Chromosome |
| 蛋白大小 | 2/10 | ×1 | 2 | 2414 aa / 264.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=994 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.2; PDB: 1L3E, 1P4Q, 2K8F, 2MH0, 2MZD, 3BIY, 3I3J |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001487, IPR036427, IPR018359, IPR031162, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- histone acetyltransferase complex (GO:0000123)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 994 |
| PubMed broad count | 2575 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: P300 |

**关键文献**:
1. Lactate reprograms glioblastoma immunity through CBX3-regulated histone lactylation.. *The Journal of clinical investigation*. PMID: 39545414
2. EP300 Selectively Controls the Enhancer Landscape of MYCN-Amplified Neuroblastoma.. *Cancer discovery*. PMID: 34772733
3. Exosome-derived circCCAR1 promotes CD8 + T-cell dysfunction and anti-PD1 resistance in hepatocellular carcinoma.. *Molecular cancer*. PMID: 36932387
4. Rubinstein-Taybi Syndrome.. **. PMID: 20301699
5. Histone lysine acetyltransferase inhibitors: an emerging class of drugs for cancer therapy.. *Trends in pharmacological sciences*. PMID: 38383216

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 61.3% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 1L3E, 1P4Q, 2K8F, 2MH0, 2MZD, 3BIY, 3I3J, 3IO2, 3P57, 3T92 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.2），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001487, IPR036427, IPR018359, IPR031162, IPR013178; Pfam: PF00439, PF09030, PF08214 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RELA | 0.999 | 0.950 | — |
| STAT3 | 0.999 | 0.856 | — |
| TP53 | 0.999 | 0.999 | — |
| JUN | 0.999 | 0.885 | — |
| HIF1A | 0.999 | 0.999 | — |
| HDAC1 | 0.999 | 0.806 | — |
| CREB1 | 0.999 | 0.875 | — |
| SMAD3 | 0.999 | 0.926 | — |
| NCOA1 | 0.999 | 0.792 | — |
| H4C6 | 0.999 | 0.999 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HIF1A | psi-mi:"MI:0096"(pull down) | pubmed:15261140 |
| EPAS1 | psi-mi:"MI:0096"(pull down) | pubmed:15261140 |
| TP53 | psi-mi:"MI:0096"(pull down) | pubmed:9194564 |
| COPS6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| His2A | psi-mi:"MI:0415"(enzymatic study) | pubmed:16415179|imex:IM-19875 |
| His3 | psi-mi:"MI:0415"(enzymatic study) | pubmed:16415179|imex:IM-19875 |
| His4r | psi-mi:"MI:0415"(enzymatic study) | pubmed:16415179|imex:IM-19875 |
| NAP1L1 | psi-mi:"MI:0096"(pull down) | pubmed:11940655|imex:IM-19548 |
| POU3F2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11029584|imex:IM-19682 |
| TFAP2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12586840|imex:IM-19636 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.2 + PDB: 1L3E, 1P4Q, 2K8F, 2MH0, 2MZD,  | pLDDT=53.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome / Nucleoplasm; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EP300 — Histone acetyltransferase p300，研究基础较多，新颖性有限。
2. 蛋白大小2414 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 994 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 994 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q09472
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100393-EP300/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EP300
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q09472
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
