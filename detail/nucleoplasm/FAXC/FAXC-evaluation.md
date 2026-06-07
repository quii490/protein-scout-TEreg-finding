---
type: protein-evaluation
gene: "FAXC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAXC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAXC / C6orf168 |
| 蛋白名称 | Failed axon connections homolog |
| 蛋白大小 | 409 aa / 46.8 kDa |
| UniProt ID | Q5TGI0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 409 aa / 46.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026928, IPR045796, IPR036282, IPR040079, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf168 |

**关键文献**:
1. Clinical course of a Japanese patient with developmental delay linked to a small 6q16.1 deletion.. *Human genome variation*. PMID: 35581197
2. FAXC depletion contributes to tumor progression via the c-MET pathway in renal cell carcinoma.. *Biochemical and biophysical research communications*. PMID: 40706244

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 29.1% |
| 有序区域 (pLDDT>70) 占比 | 65.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.6，有序区 65.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026928, IPR045796, IPR036282, IPR040079, IPR033468; Pfam: PF19333, PF17171, PF17172 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ3 | 0.605 | 0.000 | — |
| PNISR | 0.570 | 0.000 | — |
| USP45 | 0.560 | 0.000 | — |
| QSER1 | 0.556 | 0.000 | — |
| FBXL4 | 0.553 | 0.000 | — |
| TEX9 | 0.542 | 0.000 | — |
| DSTYK | 0.535 | 0.071 | — |
| TMTC2 | 0.522 | 0.000 | — |
| NUFIP2 | 0.499 | 0.000 | — |
| CCNC | 0.482 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 无 | pLDDT=74.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
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
1. FAXC — Failed axon connections homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小409 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TGI0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146267-FAXC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAXC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TGI0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000146267-FAXC/subcellular

![](https://images.proteinatlas.org/39106/435_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/39106/435_G9_3_red_green.jpg)
![](https://images.proteinatlas.org/39106/445_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/39106/445_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/39106/448_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/39106/448_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5TGI0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5TGI0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026928;IPR045796;IPR036282;IPR040079;IPR033468;IPR050931;IPR012336;IPR036249; |
| Pfam | PF19333;PF17171;PF17172; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146267-FAXC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHCHD3 | Bioplex | false |
| CHCHD6 | Bioplex | false |
| DDX20 | Bioplex | false |
| KNTC1 | Bioplex | false |
| MTX2 | Bioplex | false |
| MTX3 | Bioplex | false |
| PGBD1 | Bioplex | false |
| PGBD2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
