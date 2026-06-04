---
type: protein-evaluation
gene: "ITSN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ITSN1 — REJECTED (研究热度过高 (PubMed strict=105，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ITSN1 / ITSN, SH3D1A |
| 蛋白名称 | Intersectin-1 |
| 蛋白大小 | 1721 aa / 195.4 kDa |
| UniProt ID | Q15811 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Endomembrane system; Synapse, synaptosome; Cell projection,  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1721 aa / 195.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=105 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.3; PDB: 1KI1, 2KGR, 2KHN, 3FIA, 3QBV, 4IIM, 5HZI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR035899, IPR000219, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Supported |
| UniProt | Endomembrane system; Synapse, synaptosome; Cell projection, lamellipodium; Cell membrane; Membrane, ... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical dendrite (GO:0097440)
- clathrin-coated pit (GO:0005905)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- glutamatergic synapse (GO:0098978)
- intracellular vesicle (GO:0097708)
- lamellipodium (GO:0030027)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 105 |
| PubMed broad count | 163 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ITSN, SH3D1A |

**关键文献**:
1. ITSN1: a novel candidate gene involved in autosomal dominant neurodevelopmental disorder spectrum.. *European journal of human genetics : EJHG*. PMID: 34707297
2. Intersectin1 promotes clathrin-mediated endocytosis by organizing and stabilizing endocytic protein interaction networks.. *Cell reports*. PMID: 39580802
3. Intersectin-1 enhances calcium-dependent replenishment of the readily releasable pool of synaptic vesicles during development.. *The Journal of physiology*. PMID: 39383250
4. The alternative splicing of intersectin 1 regulated by PTBP1 promotes human glioma progression.. *Cell death & disease*. PMID: 36171198
5. Environmental enrichment improves social isolation-induced memory impairment: The possible role of ITSN1-Reelin-AMPA receptor signaling pathway.. *PloS one*. PMID: 38241230

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.3 |
| 高置信度残基 (pLDDT>90) 占比 | 33.2% |
| 置信残基 (pLDDT 70-90) 占比 | 33.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 24.2% |
| 有序区域 (pLDDT>70) 占比 | 66.8% |
| 可用 PDB 条目 | 1KI1, 2KGR, 2KHN, 3FIA, 3QBV, 4IIM, 5HZI, 5HZJ, 5HZK, 6GBU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1KI1, 2KGR, 2KHN, 3FIA, 3QBV, 4IIM, 5HZI, 5HZJ, 5HZK, 6GBU）+ AlphaFold极高置信度预测（pLDDT=72.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR035899, IPR000219, IPR011992; Pfam: PF00168, PF12763, PF16617 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.999 | 0.979 | — |
| WASL | 0.999 | 0.535 | — |
| FCHO1 | 0.999 | 0.330 | — |
| EPS15 | 0.997 | 0.731 | — |
| AP2B1 | 0.992 | 0.978 | — |
| EPN2 | 0.992 | 0.283 | — |
| FCHO2 | 0.985 | 0.330 | — |
| STON2 | 0.983 | 0.292 | — |
| DNM1 | 0.979 | 0.711 | — |
| EPN3 | 0.970 | 0.108 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDC42 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12006984 |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KIF5A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MRPL20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SNX5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SMARCC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12812986|imex:IM-19614 |
| SMNDC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| A0A1Q4LW06 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.3 + PDB: 1KI1, 2KGR, 2KHN, 3FIA, 3QBV,  | pLDDT=72.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endomembrane system; Synapse, synaptosome; Cell pr / Plasma membrane; 额外: Nucleoplasm | 一致 |
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
1. ITSN1 — Intersectin-1，研究基础较多，新颖性有限。
2. 蛋白大小1721 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 105 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 105 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15811
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205726-ITSN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ITSN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15811
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
