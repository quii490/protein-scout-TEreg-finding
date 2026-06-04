---
type: protein-evaluation
gene: "LIMD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LIMD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LIMD1 |
| 蛋白名称 | LIM domain-containing protein 1 |
| 蛋白大小 | 676 aa / 72.2 kDa |
| UniProt ID | Q9UGP4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Focal adhesion sites; UniProt: Cytoplasm; Nucleus; Cytoplasm, P-body; Cell junction, adhere |
| 蛋白大小 | 10/10 | ×1 | 10 | 676 aa / 72.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047172, IPR047245, IPR047247, IPR047248, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Focal adhesion sites | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, P-body; Cell junction, adherens junction; Cell junction, focal adhesi... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- P-body (GO:0000932)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 100 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. TRIP6 is required for tension at adherens junctions.. *Journal of cell science*. PMID: 33558314
2. Clinical implications of activation of the LIMD1-VHL-HIF1α pathway during head-&-neck squamous cell carcinoma development.. *The Indian journal of medical research*. PMID: 39382421
3. A HIF-LIMD1 negative feedback mechanism mitigates the pro-tumorigenic effects of hypoxia.. *EMBO molecular medicine*. PMID: 29930174
4. LncRNA-mir3471-limd1 regulatory network plays critical roles in HIBD.. *Experimental brain research*. PMID: 38147087
5. Targeted therapy for LIMD1-deficient non-small cell lung cancer subtypes.. *Cell death & disease*. PMID: 34764236

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.2% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 55.8% |
| 有序区域 (pLDDT>70) 占比 | 36.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 36.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047172, IPR047245, IPR047247, IPR047248, IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LATS1 | 0.995 | 0.712 | — |
| LATS2 | 0.966 | 0.564 | — |
| SAV1 | 0.964 | 0.134 | — |
| TNRC6A | 0.959 | 0.292 | — |
| EIF4E | 0.943 | 0.000 | — |
| AGO1 | 0.941 | 0.292 | — |
| DDX6 | 0.939 | 0.300 | — |
| AGO2 | 0.936 | 0.292 | — |
| AJUBA | 0.925 | 0.233 | — |
| DICER1 | 0.913 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| lepB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GFI1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17909014|imex:IM-18884 |
| ORF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| gag-pol | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| STAC | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| MAP3K6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHYHIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C1orf105 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 无 | pLDDT=56.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, P-body; Cell juncti / Nucleoplasm, Focal adhesion sites | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LIMD1 — LIM domain-containing protein 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小676 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UGP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144791-LIMD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LIMD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UGP4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
