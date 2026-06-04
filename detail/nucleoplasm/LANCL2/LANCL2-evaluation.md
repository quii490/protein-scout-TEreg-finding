---
type: protein-evaluation
gene: "LANCL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LANCL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LANCL2 / GPR69B, TASP |
| 蛋白名称 | LanC-like protein 2 |
| 蛋白大小 | 450 aa / 50.9 kDa |
| UniProt ID | Q9NS86 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 450 aa / 50.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.0; PDB: 6WQ1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012341, IPR007822, IPR020464; Pfam: PF05147 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cortical actin cytoskeleton (GO:0030864)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPR69B, TASP |

**关键文献**:
1. G-protein coupling and nuclear translocation of the human abscisic acid receptor LANCL2.. *Scientific reports*. PMID: 27222287
2. LanCL2 Implicates in Testicular Redox Homeostasis and Acrosomal Maturation.. *Antioxidants (Basel, Switzerland)*. PMID: 38790639
3. Lanthionine synthetase C-like protein 2 (LanCL2) is important for adipogenic differentiation.. *Journal of lipid research*. PMID: 29880530
4. Phytohormone abscisic acid ameliorates neuropathic pain via regulating LANCL2 protein abundance and glial activation at the spinal cord.. *Molecular pain*. PMID: 35647699
5. LANCL2 is necessary for abscisic acid binding and signaling in human granulocytes and in rat insulinoma cells.. *The Journal of biological chemistry*. PMID: 19667068

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.0 |
| 高置信度残基 (pLDDT>90) 占比 | 86.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 5.3% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 6WQ1 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.0，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012341, IPR007822, IPR020464; Pfam: PF05147 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPS8 | 0.706 | 0.000 | — |
| VOPP1 | 0.682 | 0.000 | — |
| SEC61G | 0.639 | 0.000 | — |
| EGFR | 0.628 | 0.165 | — |
| ECD | 0.599 | 0.000 | — |
| MINDY3 | 0.596 | 0.595 | — |
| ABCB1 | 0.584 | 0.000 | — |
| SEPTIN14 | 0.570 | 0.000 | — |
| VSTM2A | 0.543 | 0.000 | — |
| DOK2 | 0.532 | 0.532 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Map2k5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| OTUD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| GMFG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GSTM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PVR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APPBP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TDRKH | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SIAH1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.0 + PDB: 6WQ1 | pLDDT=92.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LANCL2 — LanC-like protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小450 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS86
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132434-LANCL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LANCL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS86
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
