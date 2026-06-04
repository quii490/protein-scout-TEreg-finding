---
type: protein-evaluation
gene: "TUSC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TUSC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TUSC1 |
| 蛋白名称 | Tumor suppressor candidate gene 1 protein |
| 蛋白大小 | 209 aa / 23.1 kDa |
| UniProt ID | Q2TAM9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 209 aa / 23.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043450 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Association of TUSC1 and DPF3 gene polymorphisms with male infertility.. *Journal of assisted reproduction and genetics*. PMID: 28975488
2. Circular RNA circ_0065378 upregulates tumor suppressor candidate 1 by competitively binding with miR-4701-5p to alleviate colorectal cancer progression.. *Journal of gastroenterology and hepatology*. PMID: 35434854
3. TUSC1, a putative tumor suppressor gene, reduces tumor cell growth in vitro and tumor growth in vivo.. *PloS one*. PMID: 23776618
4. Arsenic-gene interactions and beta-cell function in the Strong Heart Family Study.. *Toxicology and applied pharmacology*. PMID: 29621497
5. Tumor Suppressor Candidate 1 Suppresses Cell Growth and Predicts Better Survival in Glioblastoma.. *Cellular and molecular neurobiology*. PMID: 26897357

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 37.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 44.5% |
| 有序区域 (pLDDT>70) 占比 | 43.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 43.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043450 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GGPS1 | 0.543 | 0.543 | — |
| RFX8 | 0.486 | 0.000 | — |
| IZUMO3 | 0.435 | 0.000 | — |
| ZNF197 | 0.412 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GGPS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TACC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| EIF3D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EBI-2532663 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |
| ORF66 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |
| EBI-2532212 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 7
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 无 | pLDDT=67.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 4 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TUSC1 — Tumor suppressor candidate gene 1 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小209 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2TAM9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198680-TUSC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TUSC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TAM9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
