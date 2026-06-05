---
type: protein-evaluation
gene: "SSRP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SSRP1 — REJECTED (研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SSRP1 / FACT80 |
| 蛋白名称 | FACT complex subunit SSRP1 |
| 蛋白大小 | 709 aa / 81.1 kDa |
| UniProt ID | Q08945 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli, Centrosome; UniProt: Nucleus; Nucleus, nucleolus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 709 aa / 81.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=146 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.2; PDB: 4IFS, 5UMR, 5UMS, 5VWE, 6L1E, 6L1R, 6L34 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR011993, IPR013719, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Centrosome | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- FACT complex (GO:0035101)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 283 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FACT80 |

**关键文献**:
1. The Current Status of SSRP1 in Cancer: Tribulation and Road Ahead.. *Journal of healthcare engineering*. PMID: 35463672
2. FACT subunit SUPT16H associates with BRD4 and contributes to silencing of interferon signaling.. *Nucleic acids research*. PMID: 35904816
3. Pseudokinase TRIB3 stabilizes SSRP1 via USP10-mediated deubiquitination to promote multiple myeloma progression.. *Oncogene*. PMID: 39653795
4. SSRP1 affects the growth and apoptosis of gastric cancer cells through AKT pathway.. *Journal of medical biochemistry*. PMID: 35291495
5. Mir204 and Mir211 suppress synovial inflammation and proliferation in rheumatoid arthritis by targeting Ssrp1.. *eLife*. PMID: 36511897

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 26.4% |
| 置信残基 (pLDDT 70-90) 占比 | 42.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| 可用 PDB 条目 | 4IFS, 5UMR, 5UMS, 5VWE, 6L1E, 6L1R, 6L34, 6UPK, 6UPL, 9EH2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4IFS, 5UMR, 5UMS, 5VWE, 6L1E, 6L1R, 6L34, 6UPK, 6UPL, 9EH2）+ AlphaFold极高置信度预测（pLDDT=74.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR011993, IPR013719, IPR050454; Pfam: PF00505, PF21103, PF17292 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUPT16H | 0.999 | 0.998 | — |
| SUPT6H | 0.993 | 0.847 | — |
| RTF1 | 0.992 | 0.963 | — |
| LEO1 | 0.991 | 0.962 | — |
| H3C12 | 0.990 | 0.969 | — |
| CTR9 | 0.989 | 0.944 | — |
| SUPT5H | 0.989 | 0.854 | — |
| H4C6 | 0.988 | 0.983 | — |
| PAF1 | 0.985 | 0.963 | — |
| POLR2A | 0.982 | 0.873 | — |

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
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 4IFS, 5UMR, 5UMS, 5VWE, 6L1E,  | pLDDT=74.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Chromosome / Nucleoplasm; 额外: Nucleoli, Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SSRP1 — FACT complex subunit SSRP1，研究基础较多，新颖性有限。
2. 蛋白大小709 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 146 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08945
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149136-SSRP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SSRP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08945
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000149136-SSRP1/subcellular

![](https://images.proteinatlas.org/2696/1867_A2_10_cr5b630c26c9b38_red_green.jpg)
![](https://images.proteinatlas.org/2696/1867_A2_16_cr5b630c26ca233_red_green.jpg)
![](https://images.proteinatlas.org/2696/2088_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/2696/2088_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/2696/2197_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/2696/2197_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08945-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
