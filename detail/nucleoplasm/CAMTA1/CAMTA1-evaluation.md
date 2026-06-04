---
type: protein-evaluation
gene: "CAMTA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAMTA1 — REJECTED (研究热度过高 (PubMed strict=151，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAMTA1 / KIAA0833 |
| 蛋白名称 | Calmodulin-binding transcription activator 1 |
| 蛋白大小 | 1673 aa / 183.7 kDa |
| UniProt ID | Q9Y6Y1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli, Basal body; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1673 aa / 183.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=151 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.6; PDB: 2CXK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR005559, IPR013783, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Basal body | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 151 |
| PubMed broad count | 262 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0833 |

**关键文献**:
1. The role of inflammation and genetics in periodontal disease.. *Periodontology 2000*. PMID: 32385877
2. Penetrance, variable expressivity and monogenic neurodevelopmental disorders.. *European journal of medical genetics*. PMID: 38453051
3. [Epithelioid hemangioendothelioma].. *Bulletin du cancer*. PMID: 30527817
4. Methylome analysis of FTLD patients with TDP-43 pathology identifies epigenetic signatures specific to pathological subtypes.. *Molecular neurodegeneration*. PMID: 40619440
5. CAMTA1-PPP3CA-NFATc4 multi-protein complex mediates the resistance of colorectal cancer to oxaliplatin.. *Cell death discovery*. PMID: 35332122

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.6 |
| 高置信度残基 (pLDDT>90) 占比 | 11.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 63.7% |
| 有序区域 (pLDDT>70) 占比 | 30.6% |
| 可用 PDB 条目 | 2CXK |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.6），有序残基占 30.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR005559, IPR013783, IPR014756; Pfam: PF12796, PF03859, PF00612 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WWTR1 | 0.864 | 0.000 | — |
| CALM3 | 0.765 | 0.000 | — |
| TFE3 | 0.714 | 0.000 | — |
| VAMP3 | 0.660 | 0.000 | — |
| CALML3 | 0.597 | 0.000 | — |
| CALML5 | 0.596 | 0.000 | — |
| CALML4 | 0.595 | 0.000 | — |
| CALML6 | 0.595 | 0.000 | — |
| NPPA | 0.579 | 0.000 | — |
| ANK2 | 0.542 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ALB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| Rab32 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |
| CHCHD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IPO5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AIFM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| N | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:34232536|imex:IM-29365 |
| PEX14 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.6 + PDB: 2CXK | pLDDT=50.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol; 额外: Nucleoli, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. CAMTA1 — Calmodulin-binding transcription activator 1，研究基础较多，新颖性有限。
2. 蛋白大小1673 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 151 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 151 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6Y1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171735-CAMTA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAMTA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6Y1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
