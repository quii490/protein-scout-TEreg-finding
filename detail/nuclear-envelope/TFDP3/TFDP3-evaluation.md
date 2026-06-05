---
type: protein-evaluation
gene: "TFDP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TFDP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFDP3 / DP4, HCA661 |
| 蛋白名称 | Transcription factor Dp family member 3 |
| 蛋白大小 | 405 aa / 45.0 kDa |
| UniProt ID | Q5H9I0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 405 aa / 45.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037241, IPR003316, IPR038168, IPR014889, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DP4, HCA661 |

**关键文献**:
1. TFDP3 as E2F Unique Partner, Has Crucial Roles in Cancer Cells and Testis.. *Frontiers in oncology*. PMID: 34745961
2. Cancer testis antigens in myelodysplastic syndromes revisited: a targeted RNA-seq approach.. *Oncoimmunology*. PMID: 33101773
3. Human TFDP3, a novel DP protein, inhibits DNA binding and transactivation by E2F.. *The Journal of biological chemistry*. PMID: 17062573
4. TFDP3 regulates the apoptosis and autophagy in breast cancer cell line MDA-MB-231.. *PloS one*. PMID: 30235236
5. TFDP3 Regulates Epithelial-Mesenchymal Transition in Breast Cancer.. *PloS one*. PMID: 28114432

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 43.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 39.5% |
| 有序区域 (pLDDT>70) 占比 | 52.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 52.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037241, IPR003316, IPR038168, IPR014889, IPR015648; Pfam: PF08781, PF02319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| E2F4 | 0.932 | 0.630 | — |
| HRK | 0.916 | 0.000 | — |
| E2F5 | 0.907 | 0.401 | — |
| E2F8 | 0.900 | 0.194 | — |
| E2F7 | 0.892 | 0.194 | — |
| E2F6 | 0.889 | 0.401 | — |
| E2F3 | 0.884 | 0.687 | — |
| APC | 0.884 | 0.000 | — |
| DPP8 | 0.855 | 0.000 | — |
| E2F1 | 0.848 | 0.401 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| MLF1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| HSF2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| NUDC | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| NUDCD3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| SGTA | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| EBI-9356686 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| STUB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| CACYBP | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| AARSD1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 无 | pLDDT=67.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Nuclear membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. TFDP3 — Transcription factor Dp family member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小405 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5H9I0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183434-TFDP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFDP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5H9I0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000183434-TFDP3/subcellular

![](https://images.proteinatlas.org/77304/1924_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/77304/1924_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/77304/1979_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/77304/1979_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/77304/2038_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/77304/2038_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5H9I0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
