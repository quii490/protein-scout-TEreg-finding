---
type: protein-evaluation
gene: "FANCL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCL — REJECTED (研究热度过高 (PubMed strict=114，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCL / PHF9 |
| 蛋白名称 | E3 ubiquitin-protein ligase FANCL |
| 蛋白大小 | 375 aa / 42.9 kDa |
| UniProt ID | Q9NW38 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 375 aa / 42.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=114 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.3; PDB: 3ZQS, 4CCG, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026848, IPR026850, IPR043898, IPR044037, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- nuclear body (GO:0016604)
- nuclear envelope (GO:0005635)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 114 |
| PubMed broad count | 372 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PHF9 |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. Deficient FANCL Predisposes to Endothelial Damage: A New Therapeutic Target for Pulmonary Hypertension.. *American journal of respiratory and critical care medicine*. PMID: 40479584
3. FANCL gene mutations in premature ovarian insufficiency.. *Human mutation*. PMID: 32048394
4. FANCL supports Parkin-mediated mitophagy in a ubiquitin ligase-independent manner.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 35644338
5. Deficiency of the Fanconi anemia core complex protein FAAP100 results in severe Fanconi anemia.. *The Journal of clinical investigation*. PMID: 40244696

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.3 |
| 高置信度残基 (pLDDT>90) 占比 | 76.0% |
| 置信残基 (pLDDT 70-90) 占比 | 19.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 95.7% |
| 可用 PDB 条目 | 3ZQS, 4CCG, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3ZQS, 4CCG, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=91.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026848, IPR026850, IPR043898, IPR044037, IPR043003; Pfam: PF11793, PF09765, PF18890 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HES1 | 0.999 | 0.994 | — |
| FAAP100 | 0.999 | 0.998 | — |
| FANCG | 0.999 | 0.998 | — |
| FANCB | 0.999 | 0.998 | — |
| FANCM | 0.999 | 0.994 | — |
| FANCC | 0.999 | 0.998 | — |
| FANCD2 | 0.999 | 0.980 | — |
| FAAP24 | 0.999 | 0.994 | — |
| FANCA | 0.999 | 0.998 | — |
| CENPS | 0.999 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| UBE2W | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| SRGAP3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP11-1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HDHD3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KIFC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP19-6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CHCHD3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP13-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.3 + PDB: 3ZQS, 4CCG, 7KZP, 7KZQ, 7KZR,  | pLDDT=91.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear bodies; 额外: Vesicles | 一致 |
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
1. FANCL — E3 ubiquitin-protein ligase FANCL，研究基础较多，新颖性有限。
2. 蛋白大小375 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 114 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 114 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NW38
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115392-FANCL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NW38
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
