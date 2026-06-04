---
type: protein-evaluation
gene: "ID1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ID1 — REJECTED (研究热度过高 (PubMed strict=1402，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ID1 / BHLHB24, ID |
| 蛋白名称 | DNA-binding protein inhibitor ID-1 |
| 蛋白大小 | 155 aa / 16.1 kDa |
| UniProt ID | P41134 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 155 aa / 16.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1402 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR026052, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1402 |
| PubMed broad count | 2129 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB24, ID |

**关键文献**:
1. The AhR-Ovol1-Id1 regulatory axis in keratinocytes promotes epidermal and immune homeostasis in atopic dermatitis-like skin inflammation.. *Cellular & molecular immunology*. PMID: 39939818
2. The non-cell-autonomous function of ID1 promotes AML progression via ANGPTL7 from the microenvironment.. *Blood*. PMID: 37319434
3. Autophagy-mediated ID1 turnover dictates chemo-resistant fate in ovarian cancer stem cells.. *Journal of experimental & clinical cancer research : CR*. PMID: 39123206
4. An attractor state zone precedes neural crest fate in melanoma initiation.. *bioRxiv : the preprint server for biology*. PMID: 39484503
5. Interplay between transforming growth factor-β and Nur77 in dual regulations of inhibitor of differentiation 1 for colonic tumorigenesis.. *Nature communications*. PMID: 33990575

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 46.5% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 32.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.5），有序残基占 32.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR026052, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXO3 | 0.989 | 0.000 | — |
| TCF3 | 0.973 | 0.898 | — |
| TCF4 | 0.972 | 0.889 | — |
| ETS2 | 0.958 | 0.000 | — |
| THBS1 | 0.957 | 0.071 | — |
| MYOD1 | 0.946 | 0.832 | — |
| TCF12 | 0.904 | 0.826 | — |
| RAP1A | 0.901 | 0.000 | — |
| RAP1B | 0.900 | 0.000 | — |
| ID3 | 0.871 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TCF4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| COPB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Cdc20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12166|pubmed:19167333 |
| CAV1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17855368 |
| Kcnma1 | psi-mi:"MI:0096"(pull down) | imex:IM-11875|pubmed:17610306 |
| PSMD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14939|pubmed:17891176 |
| TCF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:10915743|imex:IM-19434 |
| CASK | psi-mi:"MI:0018"(two hybrid) | pubmed:15694377 |
| TCF12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ASCL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.5 + PDB: 无 | pLDDT=65.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. ID1 — DNA-binding protein inhibitor ID-1，研究基础较多，新颖性有限。
2. 蛋白大小155 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1402 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1402 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41134
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125968-ID1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ID1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41134
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
