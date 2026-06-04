---
type: protein-evaluation
gene: "GPR55"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR55 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=440，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR55 |
| 蛋白名称 | G-protein coupled receptor 55 |
| 蛋白大小 | 319 aa / 36.6 kDa |
| UniProt ID | Q9Y2T6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 319 aa / 36.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=440 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.4; PDB: 8ZX4, 8ZX5, 9GE2, 9GE3, 9IY8, 9IYA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 440 |
| PubMed broad count | 643 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cannabidiol modulates excitatory-inhibitory ratio to counter hippocampal hyperactivity.. *Neuron*. PMID: 36787750
2. Anandamide and other N-acylethanolamines: A class of signaling lipids with therapeutic opportunities.. *Progress in lipid research*. PMID: 36150527
3. Novel cannabinoid receptors.. *British journal of pharmacology*. PMID: 17906678
4. Cannabinoids in Gynecological Diseases.. *Medical cannabis and cannabinoids*. PMID: 34676329
5. GPR55 in B cells limits atherosclerosis development and regulates plasma cell maturation.. *Nature cardiovascular research*. PMID: 36523570

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 58.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 8ZX4, 8ZX5, 9GE2, 9GE3, 9IY8, 9IYA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8ZX4, 8ZX5, 9GE2, 9GE3, 9IY8, 9IYA）+ AlphaFold极高置信度预测（pLDDT=87.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNA12 | 0.983 | 0.125 | — |
| CNR1 | 0.983 | 0.000 | — |
| TRPV1 | 0.922 | 0.045 | — |
| GPR119 | 0.922 | 0.000 | — |
| GNAQ | 0.899 | 0.115 | — |
| GNA13 | 0.867 | 0.125 | — |
| FAAH | 0.848 | 0.000 | — |
| ARRB2 | 0.846 | 0.452 | — |
| NAPEPLD | 0.801 | 0.000 | — |
| CNR2 | 0.793 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LGALS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HOXD13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCAMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAB29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| XPO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TM9SF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FANCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TTI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MCM3AP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 8ZX4, 8ZX5, 9GE2, 9GE3, 9IY8,  | pLDDT=87.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
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
1. GPR55 — G-protein coupled receptor 55，研究基础较多，新颖性有限。
2. 蛋白大小319 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 440 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2T6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135898-GPR55/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR55
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2T6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
