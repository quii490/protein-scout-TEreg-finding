---
type: protein-evaluation
gene: "MROH8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MROH8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MROH8 / C20orf131, C20orf132 |
| 蛋白名称 | Protein MROH8 |
| 蛋白大小 | 483 aa / 54.8 kDa |
| UniProt ID | Q9H579 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 483 aa / 54.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR055408, IPR048465, IPR045206; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf131, C20orf132 |

**关键文献**:
1. Identifying Predictive Gene Expression and Signature Related to Temozolomide Sensitivity of Glioblastomas.. *Frontiers in oncology*. PMID: 32528873
2. METTL16 inhibits pancreatic cancer proliferation and metastasis by promoting MROH8 RNA stability and inhibiting CAPN2 expression - experimental studies.. *International journal of surgery (London, England)*. PMID: 39434688

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 28.2% |
| 置信残基 (pLDDT 70-90) 占比 | 40.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 18.6% |
| 有序区域 (pLDDT>70) 占比 | 69.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 69.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR055408, IPR048465, IPR045206; Pfam: PF21047, PF23210 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OR9G1 | 0.625 | 0.000 | — |
| NUTM2G | 0.507 | 0.000 | — |
| KRTAP9-1 | 0.505 | 0.000 | — |
| BBOF1 | 0.505 | 0.000 | — |
| UBE3B | 0.494 | 0.000 | — |
| NFS1 | 0.449 | 0.000 | — |
| C3AR1 | 0.448 | 0.000 | — |
| MCRIP1 | 0.418 | 0.000 | — |
| SHANK3 | 0.417 | 0.000 | — |
| POLR3F | 0.411 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENST00000343811 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 1
- 调控相关比例: 1 / 11 = 9%

**评价**: STRING 11 个预测互作，IntAct 1 个实验互作。调控相关配体占比 9%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles, Cytosol | 待确认 |
| PPI | STRING + IntAct | 11 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MROH8 — Protein MROH8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小483 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H579
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101353-MROH8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MROH8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H579
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000101353-MROH8/subcellular

![](https://images.proteinatlas.org/58316/1873_E6_4_red_green.jpg)
![](https://images.proteinatlas.org/58316/1873_E6_5_red_green.jpg)
![](https://images.proteinatlas.org/58316/2062_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/58316/2062_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/58316/2198_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/58316/2198_G7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H579-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
