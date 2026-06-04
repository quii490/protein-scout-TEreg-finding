---
type: protein-evaluation
gene: "FANCI"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCI — REJECTED (研究热度过高 (PubMed strict=230，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCI / KIAA1794 |
| 蛋白名称 | Fanconi anemia group I protein |
| 蛋白大小 | 1328 aa / 149.3 kDa |
| UniProt ID | Q9NVI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1328 aa / 149.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=230 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.2; PDB: 6VAA, 6VAD, 6VAE, 6VAF, 7AY1, 7ZF1, 8A9J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026171, IPR029310, IPR029312, IPR029308, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- DNA repair complex (GO:1990391)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 230 |
| PubMed broad count | 496 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1794 |

**关键文献**:
1. FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions.. *Nature*. PMID: 39085614
2. Fanconi Anemia.. **. PMID: 20301575
3. Structural basis of Fanconi anemia pathway activation by FANCM.. *The EMBO journal*. PMID: 40447800
4. Structural insight into FANCI-FANCD2 monoubiquitination.. *Essays in biochemistry*. PMID: 32725171
5. Familial breast cancer and DNA repair genes: Insights into known and novel susceptibility genes from the GENESIS study, and implications for multigene panel testing.. *International journal of cancer*. PMID: 30303537

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 51.8% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 83.3% |
| 可用 PDB 条目 | 6VAA, 6VAD, 6VAE, 6VAF, 7AY1, 7ZF1, 8A9J, 8A9K |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6VAA, 6VAD, 6VAE, 6VAF, 7AY1, 7ZF1, 8A9J, 8A9K）+ AlphaFold极高置信度预测（pLDDT=83.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026171, IPR029310, IPR029312, IPR029308, IPR029305; Pfam: PF14679, PF14680, PF14675 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCA | 0.999 | 0.800 | — |
| FANCD2 | 0.999 | 0.996 | — |
| FANCG | 0.999 | 0.800 | — |
| FANCL | 0.999 | 0.967 | — |
| FANCC | 0.999 | 0.800 | — |
| FANCB | 0.999 | 0.800 | — |
| FANCE | 0.999 | 0.800 | — |
| WDR48 | 0.998 | 0.948 | — |
| FANCM | 0.998 | 0.292 | — |
| FANCF | 0.998 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NEK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RAB5IF | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGED1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 6VAA, 6VAD, 6VAE, 6VAF, 7AY1,  | pLDDT=83.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FANCI — Fanconi anemia group I protein，研究基础较多，新颖性有限。
2. 蛋白大小1328 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 230 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 230 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140525-FANCI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
