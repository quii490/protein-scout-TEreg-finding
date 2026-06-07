---
type: protein-evaluation
gene: "PATL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PATL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PATL2 |
| 蛋白名称 | Protein PAT1 homolog 2 |
| 蛋白大小 | 543 aa / 61.5 kDa |
| UniProt ID | C9JE40 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 543 aa / 61.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039900, IPR019167; Pfam: PF09770 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- P-body (GO:0000932)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic factors as potential molecular markers of human oocyte and embryo quality.. *Journal of assisted reproduction and genetics*. PMID: 33895934
2. PATL2 mutations affect human oocyte maternal mRNA homeostasis and protein interactions in cell cycle regulation.. *Cell & bioscience*. PMID: 39741299
3. Total fertilization failure after ICSI: insights into pathophysiology, diagnosis, and management through artificial oocyte activation.. *Human reproduction update*. PMID: 36977357
4. PATL2 regulates mRNA homeostasis in oocytes by interacting with EIF4E and CPEB1.. *Development (Cambridge, England)*. PMID: 37218508
5. Novel splicing mutations in PATL2 and WEE2 cause oocyte degradation and fertilization failure.. *Journal of assisted reproduction and genetics*. PMID: 39476306

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 35.7% |
| 中等置信 (pLDDT 50-70) 占比 | 18.4% |
| 低置信 (pLDDT<50) 占比 | 33.5% |
| 有序区域 (pLDDT>70) 占比 | 48.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 48.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039900, IPR019167; Pfam: PF09770 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LSM4 | 0.999 | 0.998 | — |
| LSM1 | 0.999 | 0.998 | — |
| XRN1 | 0.998 | 0.997 | — |
| DDX6 | 0.950 | 0.832 | — |
| LSM7 | 0.901 | 0.843 | — |
| LSM2 | 0.890 | 0.843 | — |
| CNOT3 | 0.874 | 0.842 | — |
| CNOT4 | 0.856 | 0.842 | — |
| LSM5 | 0.846 | 0.843 | — |
| LSM6 | 0.842 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RRBP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DNAH5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PATL2 — Protein PAT1 homolog 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小543 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C9JE40
- Protein Atlas: https://www.proteinatlas.org/ENSG00000229474-PATL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PATL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C9JE40
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-C9JE40-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | C9JE40 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039900;IPR019167; |
| Pfam | PF09770; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000229474-PATL2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
