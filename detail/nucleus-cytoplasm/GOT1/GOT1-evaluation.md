---
type: protein-evaluation
gene: "GOT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOT1 — REJECTED (研究热度过高 (PubMed strict=231，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOT1 |
| 蛋白名称 | Aspartate aminotransferase, cytoplasmic |
| 蛋白大小 | 413 aa / 46.2 kDa |
| UniProt ID | P17174 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 46.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=231 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.4; PDB: 3II0, 3WZF, 6DNA, 6DNB, 6DND, 6LIG, 8Z0E |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004839, IPR000796, IPR004838, IPR015424, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon terminus (GO:0043679)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 231 |
| PubMed broad count | 540 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Metabolic dysregulation and emerging therapeutical targets for hepatocellular carcinoma.. *Acta pharmaceutica Sinica. B*. PMID: 35256934
2. TXNIP/VDUP1 attenuates steatohepatitis via autophagy and fatty acid oxidation.. *Autophagy*. PMID: 33190588
3. Buddleoside alleviates nonalcoholic steatohepatitis by targeting the AMPK-TFEB signaling pathway.. *Autophagy*. PMID: 39936600
4. AMPK protects against alcohol-induced liver injury through UQCRC2 to up-regulate mitophagy.. *Autophagy*. PMID: 33719895
5. Glutamine, MTOR and autophagy: a multiconnection relationship.. *Autophagy*. PMID: 35470752

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.4 |
| 高置信度残基 (pLDDT>90) 占比 | 94.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 3II0, 3WZF, 6DNA, 6DNB, 6DND, 6LIG, 8Z0E |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3II0, 3WZF, 6DNA, 6DNB, 6DND, 6LIG, 8Z0E）+ AlphaFold极高置信度预测（pLDDT=96.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004839, IPR000796, IPR004838, IPR015424, IPR015421; Pfam: PF00155 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MDH2 | 0.990 | 0.061 | — |
| GPT2 | 0.984 | 0.220 | — |
| GOT2 | 0.982 | 0.085 | — |
| GPT | 0.981 | 0.000 | — |
| GLUD1 | 0.978 | 0.101 | — |
| LDHAL6B | 0.978 | 0.061 | — |
| LDHAL6A | 0.978 | 0.061 | — |
| FH | 0.978 | 0.231 | — |
| LDHC | 0.977 | 0.061 | — |
| LDHA | 0.972 | 0.061 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sty | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| eIF5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| TMEM120A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EGFR | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:20029029|imex:IM-17166 |
| ABI3BP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Kcnma1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-9475|pubmed:19423573 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.4 + PDB: 3II0, 3WZF, 6DNA, 6DNB, 6DND,  | pLDDT=96.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GOT1 — Aspartate aminotransferase, cytoplasmic，研究基础较多，新颖性有限。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 231 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 231 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17174
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120053-GOT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17174
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
