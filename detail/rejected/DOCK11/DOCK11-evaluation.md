---
type: protein-evaluation
gene: "DOCK11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK11 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK11 / ZIZ2 |
| 蛋白名称 | Dedicator of cytokinesis protein 11 |
| 蛋白大小 | 2073 aa / 237.7 kDa |
| UniProt ID | Q5JSL3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 2073 aa / 237.7 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.9; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR037809, IPR027007, IPR035892, IPR026 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.5/180** | |
| **归一化总分** | | | **52.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZIZ2 |

**关键文献**:
1. Systemic Inflammation and Normocytic Anemia in DOCK11 Deficiency.. *The New England journal of medicine*. PMID: 37342957
2. Wnt/β-Catenin Signaling Regulates Hepatitis B Virus cccDNA Levels.. *International journal of molecular sciences*. PMID: 40725188
3. A novel hemizygous nonsense variant in DOCK11 causes systemic inflammation and immunodeficiency.. *Clinical immunology (Orlando, Fla.)*. PMID: 40274249
4. Hepatitis B Virus Utilizes a Retrograde Trafficking Route via the Trans-Golgi Network to Avoid Lysosomal Degradation.. *Cellular and molecular gastroenterology and hepatology*. PMID: 36270602
5. Super-Resolution Microscopy Analysis of Hepatitis B Viral cccDNA and Host Factors.. *Viruses*. PMID: 37243264

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 36.1% |
| 置信残基 (pLDDT 70-90) 占比 | 43.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 79.1% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区 79.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR037809, IPR027007, IPR035892, IPR026791; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.937 | 0.591 | — |
| DHX37 | 0.892 | 0.000 | — |
| DHX8 | 0.880 | 0.000 | — |
| RHOJ | 0.818 | 0.281 | — |
| RHOQ | 0.724 | 0.280 | — |
| DOCK2 | 0.693 | 0.000 | — |
| RAC1 | 0.684 | 0.287 | — |
| DOCK9 | 0.629 | 0.607 | — |
| TSHZ1 | 0.614 | 0.000 | — |
| GLYAT | 0.613 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 无 | pLDDT=78.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DOCK11 — Dedicator of cytokinesis protein 11，非常新颖，仅有少数基础研究。
2. 蛋白大小2073 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JSL3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147251-DOCK11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JSL3
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:24
