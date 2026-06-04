---
type: protein-evaluation
gene: "FGF14"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FGF14 — REJECTED (研究热度过高 (PubMed strict=184，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FGF14 / FHF4 |
| 蛋白名称 | Fibroblast growth factor 14 |
| 蛋白大小 | 247 aa / 27.7 kDa |
| UniProt ID | Q92915 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 247 aa / 27.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=184 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002209, IPR008996; Pfam: PF00167 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 184 |
| PubMed broad count | 327 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FHF4 |

**关键文献**:
1. Deep Intronic FGF14 GAA Repeat Expansion in Late-Onset Cerebellar Ataxia.. *The New England journal of medicine*. PMID: 36516086
2. Autosomal dominant cerebellar ataxias: new genes and progress towards treatments.. *The Lancet. Neurology*. PMID: 37479376
3. Spinocerebellar ataxia 27B: A novel, frequent and potentially treatable ataxia.. *Clinical and translational medicine*. PMID: 38279833
4. Spinocerebellar ataxia 27B (SCA27B), a frequent late-onset cerebellar ataxia.. *Revue neurologique*. PMID: 38609751
5. Progress and challenges in sporadic late-onset cerebellar ataxias.. *Nature reviews. Neurology*. PMID: 40983776

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 58.7% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 22.7% |
| 低置信 (pLDDT<50) 占比 | 16.2% |
| 有序区域 (pLDDT>70) 占比 | 61.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.2，有序区 61.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002209, IPR008996; Pfam: PF00167 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCN8A | 0.962 | 0.660 | — |
| MAPK8IP2 | 0.773 | 0.164 | — |
| SCN2A | 0.771 | 0.138 | — |
| FGF17 | 0.713 | 0.000 | — |
| FGFR2 | 0.699 | 0.168 | — |
| FGF18 | 0.681 | 0.000 | — |
| RAP2A | 0.650 | 0.045 | — |
| KCNC3 | 0.633 | 0.042 | — |
| CACNA1A | 0.629 | 0.138 | — |
| FGFR1 | 0.628 | 0.168 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-17619 |
| HOXD12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MAOB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FUNDC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| H4C7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FKBP8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMC1A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ACACA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BCL2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EHHADH | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 无 | pLDDT=79.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FGF14 — Fibroblast growth factor 14，研究基础较多，新颖性有限。
2. 蛋白大小247 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 184 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 184 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92915
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102466-FGF14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FGF14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92915
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
