---
type: protein-evaluation
gene: "ATG16L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATG16L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATG16L2 / WDR80 |
| 蛋白名称 | Protein Atg16l2 |
| 蛋白大小 | 619 aa / 69.0 kDa |
| UniProt ID | Q8NAA4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 619 aa / 69.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=49 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045160, IPR013923, IPR015943, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Atg12-Atg5-Atg16 complex (GO:0034274)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- phagophore assembly site membrane (GO:0034045)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR80 |

**关键文献**:
1. NR3C1/Glucocorticoid receptor activation promotes pancreatic β-cell autophagy overload in response to glucolipotoxicity.. *Autophagy*. PMID: 37039556
2. The role of ATG16L2 in autophagy and disease.. *Autophagy*. PMID: 35239457
3. LSD1 promotes the FSH responsive follicle formation by regulating autophagy and repressing Wt1 in the granulosa cells.. *Science bulletin*. PMID: 38302330
4. ATG16L2 inhibits NLRP3 inflammasome activation through promoting ATG5-12-16L1 complex assembly and autophagy.. *European journal of immunology*. PMID: 35426127
5. Atg16l2 augments Nlrc4 inflammasome activation by facilitating NAIPs-NLRC4 association.. *European journal of immunology*. PMID: 39175123

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.6 |
| 高置信度残基 (pLDDT>90) 占比 | 57.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 17.8% |
| 有序区域 (pLDDT>70) 占比 | 78.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.6，有序区 78.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045160, IPR013923, IPR015943, IPR020472, IPR019775; Pfam: PF08614, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATG5 | 0.999 | 0.934 | — |
| ATG12 | 0.996 | 0.805 | — |
| WIPI1 | 0.979 | 0.520 | — |
| WIPI2 | 0.975 | 0.520 | — |
| ATG3 | 0.968 | 0.126 | — |
| RB1CC1 | 0.961 | 0.091 | — |
| RAB33B | 0.949 | 0.354 | — |
| ATG16L1 | 0.937 | 0.307 | — |
| ULK2 | 0.785 | 0.495 | — |
| ATG9B | 0.738 | 0.120 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.6 + PDB: 无 | pLDDT=80.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ATG16L2 — Protein Atg16l2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小619 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NAA4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168010-ATG16L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATG16L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NAA4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
