---
type: protein-evaluation
gene: "CD83"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CD83 — REJECTED (研究热度过高 (PubMed strict=907，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CD83 |
| 蛋白名称 | CD83 antigen |
| 蛋白大小 | 205 aa / 23.0 kDa |
| UniProt ID | Q01151 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; 额外: Nucleoli, Golgi apparatus; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 205 aa / 23.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=907 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=72.6; PDB: 5MIX, 5MJ0, 5MJ1, 5MJ2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR003599, IPR013 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Nucleoli, Golgi apparatus | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- external side of plasma membrane (GO:0009897)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 907 |
| PubMed broad count | 3259 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Formation of a protein corona on the surface of extracellular vesicles in blood plasma.. *Journal of extracellular vesicles*. PMID: 34520123
2. A novel mutation in CD83 results in the development of a unique population of CD4+ T cells.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 15322158
3. CD40L stimulates tumor-infiltrating B-cells and improves ex vivo TIL expansion.. *Journal for immunotherapy of cancer*. PMID: 40199608
4. CD83 suppresses endogenous March-I-dependent MHC class II ubiquitination, endocytosis, and degradation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40397676
5. Hypofractionated radiotherapy combined with lenalidomide improves systemic antitumor activity in mouse solid tumor models.. *Theranostics*. PMID: 38646638

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 34.6% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 21.5% |
| 有序区域 (pLDDT>70) 占比 | 56.1% |
| 可用 PDB 条目 | 5MIX, 5MJ0, 5MJ1, 5MJ2 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5MIX, 5MJ0, 5MJ1, 5MJ2）+ AlphaFold高质量预测（pLDDT=72.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR003599, IPR013106; Pfam: PF07686 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF4E | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| A0A384LAQ1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BTAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RHOBTB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGFR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BMPR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIGA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| USP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTOR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 5MIX, 5MJ0, 5MJ1, 5MJ2 | pLDDT=72.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Plasma membrane; 额外: Nucleoli, Golgi  | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CD83 — CD83 antigen，研究基础较多，新颖性有限。
2. 蛋白大小205 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 907 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 907 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01151
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112149-CD83/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CD83
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01151
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
