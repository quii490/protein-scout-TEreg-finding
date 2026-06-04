---
type: protein-evaluation
gene: "DOCK9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK9 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK9 / KIAA1058, ZIZ1 |
| 蛋白名称 | Dedicator of cytokinesis protein 9 |
| 蛋白大小 | 2069 aa / 236.4 kDa |
| UniProt ID | Q9BZ29 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endomembrane system |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 2069 aa / 236.4 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.8; PDB: 1WG7, 2WM9, 2WMN, 2WMO |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR037809, IPR027007, IPR035892, IPR026 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endomembrane system | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endomembrane system (GO:0012505)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1058, ZIZ1 |

**关键文献**:
1. DOCK9 antisense RNA2 interacts with LIN28B to stabilize Wnt5a and boosts proliferation and migration of oxidized low densitylipoprotein-induced vascular smooth muscle cells.. *Bioengineered*. PMID: 35282771
2. DOCK9 as a predictive biomarker linked to angiogenesis and immune response in esophageal squamous cell carcinoma.. *Clinical and experimental medicine*. PMID: 40272582
3. Genetic insights into associations of multisite chronic pain with common diseases and biomarkers using data from the UK Biobank.. *British journal of anaesthesia*. PMID: 38104003
4. Roles of the DOCK-D family proteins in a mouse model of neuroinflammation.. *The Journal of biological chemistry*. PMID: 32241915
5. Variant c.2262A>C in DOCK9 Leads to Exon Skipping in Keratoconus Family.. *Investigative ophthalmology & visual science*. PMID: 26641546

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.8 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 39.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 78.6% |
| 可用 PDB 条目 | 1WG7, 2WM9, 2WMN, 2WMO |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1WG7, 2WM9, 2WMN, 2WMO）+ AlphaFold高质量预测（pLDDT=78.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR037809, IPR027007, IPR035892, IPR026791; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.977 | 0.716 | — |
| DHX8 | 0.937 | 0.000 | — |
| DHX37 | 0.897 | 0.000 | — |
| RAC1 | 0.704 | 0.255 | — |
| RABIF | 0.667 | 0.000 | — |
| RHOJ | 0.650 | 0.249 | — |
| VSX1 | 0.645 | 0.000 | — |
| DOCK11 | 0.629 | 0.607 | — |
| DOCK10 | 0.623 | 0.447 | — |
| DOCK1 | 0.569 | 0.129 | — |

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
| 三维结构 | AlphaFold pLDDT=78.8 + PDB: 1WG7, 2WM9, 2WMN, 2WMO | pLDDT=78.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endomembrane system / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DOCK9 — Dedicator of cytokinesis protein 9，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小2069 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZ29
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088387-DOCK9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZ29
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:53
