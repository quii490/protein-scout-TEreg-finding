---
type: protein-evaluation
gene: "SERPINB10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERPINB10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERPINB10 / PI10 |
| 蛋白名称 | Serpin B10 |
| 蛋白大小 | 397 aa / 45.4 kDa |
| UniProt ID | P48595 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 397 aa / 45.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023795, IPR023796, IPR000215, IPR036186, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- ficolin-1-rich granule membrane (GO:0101003)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- secretory granule membrane (GO:0030667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PI10 |

**关键文献**:
1. The effects of inhaled corticosteroids on healthy airways.. *Allergy*. PMID: 38686450
2. SERPINB10 promotes macrophage M2 polarization and airway inflammation in asthma.. *Respiratory research*. PMID: 40349036
3. Epithelial SERPINB10, a novel marker of airway eosinophilia in asthma, contributes to allergic airway inflammation.. *American journal of physiology. Lung cellular and molecular physiology*. PMID: 30382768
4. Increased SERPINB10 Expression in Induced Sputum Was Associated with Airway Type 2 Inflammation in Asthma.. *International archives of allergy and immunology*. PMID: 35526531
5. Gene expression in the chicken caecum in response to infections with non-typhoid Salmonella.. *Veterinary research*. PMID: 25475706

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 74.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 8.1% |
| 有序区域 (pLDDT>70) 占比 | 89.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.7，有序区 89.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023795, IPR023796, IPR000215, IPR036186, IPR042178; Pfam: PF00079 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTSG | 0.924 | 0.045 | — |
| LYG2 | 0.521 | 0.051 | — |
| BPIFB1 | 0.472 | 0.000 | — |
| SERPINB4 | 0.453 | 0.000 | — |
| CRISP3 | 0.442 | 0.000 | — |
| SLC14A1 | 0.406 | 0.000 | — |
| AGO2 | 0.404 | 0.000 | — |
| IVNS1ABP | 0.402 | 0.045 | — |
| UPK1B | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| KLK10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 2
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 无 | pLDDT=88.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 9 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SERPINB10 — Serpin B10，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小397 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48595
- Protein Atlas: https://www.proteinatlas.org/ENSG00000242550-SERPINB10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERPINB10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48595
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
