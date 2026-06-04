---
type: protein-evaluation
gene: "TEX55"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX55 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX55 / C3orf30, TSCPA |
| 蛋白名称 | Testis-specific expressed protein 55 |
| 蛋白大小 | 536 aa / 60.2 kDa |
| UniProt ID | Q96M34 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Plasma membrane, Cytosol; UniProt: Nucleus; Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | ×1 | 10 | 536 aa / 60.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040760, IPR048377; Pfam: PF17819 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Plasma membrane, Cytosol | Approved |
| UniProt | Nucleus; Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)
- sperm flagellum (GO:0036126)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf30, TSCPA |

**关键文献**:
1. Tex55 encodes a conserved putative A-kinase anchoring protein dispensable for male fertility in the mouse.. *Biology of reproduction*. PMID: 33458765

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.4 |
| 高置信度残基 (pLDDT>90) 占比 | 7.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 78.4% |
| 有序区域 (pLDDT>70) 占比 | 8.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.4），有序残基占 8.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040760, IPR048377; Pfam: PF17819 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRSS54 | 0.679 | 0.000 | — |
| TEX37 | 0.639 | 0.000 | — |
| EFCAB10 | 0.639 | 0.000 | — |
| GOLGA6L6 | 0.602 | 0.000 | — |
| PRSS55 | 0.587 | 0.000 | — |
| CATIP | 0.581 | 0.000 | — |
| ROPN1B | 0.570 | 0.000 | — |
| RIIAD1 | 0.528 | 0.000 | — |
| TPGS1 | 0.526 | 0.000 | — |
| GOLGA6L2 | 0.522 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.4 + PDB: 无 | pLDDT=48.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cell projection, cilium, flagellum / Nucleoplasm; 额外: Vesicles, Plasma membrane, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TEX55 — Testis-specific expressed protein 55，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小536 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96M34
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163424-TEX55/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX55
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96M34
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
