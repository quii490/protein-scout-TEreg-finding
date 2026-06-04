---
type: protein-evaluation
gene: "GPI"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPI — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=5594，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPI |
| 蛋白名称 | Glucose-6-phosphate isomerase |
| 蛋白大小 | 558 aa / 63.1 kDa |
| UniProt ID | P06744 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm; Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 63.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=5594 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.9; PDB: 1IAT, 1IRI, 1JIQ, 1JLH, 1NUH, 6XUH, 6XUI |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001672, IPR023096, IPR018189, IPR046348, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane | Approved |
| UniProt | Cytoplasm; Secreted | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary membrane (GO:0060170)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- membrane (GO:0016020)
- secretory granule lumen (GO:0034774)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5594 |
| PubMed broad count | 22874 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Biosynthesis and biology of mammalian GPI-anchored proteins.. *Open biology*. PMID: 32156170
2. Glycosylphosphatidylinositol (GPI)-anchored proteins.. *Biological & pharmaceutical bulletin*. PMID: 11995915
3. PIG-tailed membrane proteins.. *Essays in biochemistry*. PMID: 7925314
4. A fungal GPI-anchored protein gene functions as a virulence and antiviral factor.. *Cell reports*. PMID: 36223750
5. Biosynthesis and deficiencies of glycosylphosphatidylinositol.. *Proceedings of the Japan Academy. Series B, Physical and biological sciences*. PMID: 24727937

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.9 |
| 高置信度残基 (pLDDT>90) 占比 | 98.4% |
| 置信残基 (pLDDT 70-90) 占比 | 1.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.2% |
| 有序区域 (pLDDT>70) 占比 | 99.8% |
| 可用 PDB 条目 | 1IAT, 1IRI, 1JIQ, 1JLH, 1NUH, 6XUH, 6XUI, 8BBH, 8P2K, 9FCW |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1IAT, 1IRI, 1JIQ, 1JLH, 1NUH, 6XUH, 6XUI, 8BBH, 8P2K, 9FCW）+ AlphaFold极高置信度预测（pLDDT=97.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001672, IPR023096, IPR018189, IPR046348, IPR035476; Pfam: PF00342 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| G6PD | 0.999 | 0.000 | — |
| TPI1 | 0.999 | 0.394 | — |
| H6PD | 0.999 | 0.000 | — |
| MPI | 0.998 | 0.000 | — |
| TKT | 0.997 | 0.187 | — |
| PFKM | 0.997 | 0.096 | — |
| PFKL | 0.996 | 0.096 | — |
| PFKP | 0.996 | 0.096 | — |
| TKTL2 | 0.995 | 0.000 | — |
| GAPDH | 0.995 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GPAA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIGT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PIGN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPI16 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PIGK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIGS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| GAA1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| PIGH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MPPE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PIGP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.9 + PDB: 1IAT, 1IRI, 1JIQ, 1JLH, 1NUH,  | pLDDT=97.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Secreted / Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPI — Glucose-6-phosphate isomerase，研究基础较多，新颖性有限。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5594 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P06744
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105220-GPI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P06744
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
