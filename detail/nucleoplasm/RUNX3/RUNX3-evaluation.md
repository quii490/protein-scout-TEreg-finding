---
type: protein-evaluation
gene: "RUNX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RUNX3 — REJECTED (研究热度过高 (PubMed strict=1019，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RUNX3 / AML2, CBFA3, PEBP2A3 |
| 蛋白名称 | Runt-related transcription factor 3 |
| 蛋白大小 | 415 aa / 44.4 kDa |
| UniProt ID | Q13761 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 415 aa / 44.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1019 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.6; PDB: 5W69 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000040, IPR008967, IPR012346, IPR013524, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- core-binding factor complex (GO:0016513)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1019 |
| PubMed broad count | 1765 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AML2, CBFA3, PEBP2A3 |

**关键文献**:
1. Runx3 programs CD8(+) T cell residency in non-lymphoid tissues and tumours.. *Nature*. PMID: 29211713
2. Human skin-resident CD8(+) T cells require RUNX2 and RUNX3 for induction of cytotoxicity and expression of the integrin CD49a.. *Immunity*. PMID: 37269830
3. p53 Deficiency-Dependent Oncogenicity of Runx3.. *Cells*. PMID: 37190031
4. RUNX3-Mediated Immune Cell Development and Maturation.. *Critical reviews in immunology*. PMID: 29717663
5. Runx3 in Immunity, Inflammation and Cancer.. *Advances in experimental medicine and biology*. PMID: 28299669

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.6 |
| 高置信度残基 (pLDDT>90) 占比 | 28.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 56.1% |
| 有序区域 (pLDDT>70) 占比 | 32.1% |
| 可用 PDB 条目 | 5W69 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.6），有序残基占 32.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000040, IPR008967, IPR012346, IPR013524, IPR013711; Pfam: PF00853, PF08504 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBFB | 0.999 | 0.905 | — |
| TBX21 | 0.991 | 0.091 | — |
| RUNX1 | 0.980 | 0.000 | — |
| CTNNB1 | 0.977 | 0.292 | — |
| ZFHX3 | 0.955 | 0.000 | — |
| SMAD3 | 0.954 | 0.608 | — |
| EP300 | 0.948 | 0.513 | — |
| TP53 | 0.936 | 0.292 | — |
| RUNX2 | 0.933 | 0.610 | — |
| SRC | 0.933 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=60.6 + PDB: 5W69 | pLDDT=60.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Vesicles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RUNX3 — Runt-related transcription factor 3，研究基础较多，新颖性有限。
2. 蛋白大小415 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1019 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1019 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13761
- Protein Atlas: https://www.proteinatlas.org/ENSG00000020633-RUNX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RUNX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13761
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000020633-RUNX3/subcellular

![](https://images.proteinatlas.org/4195/1125_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/4195/1125_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/4195/1183_F11_5_red_green.jpg)
![](https://images.proteinatlas.org/4195/1183_F11_6_red_green.jpg)
![](https://images.proteinatlas.org/4195/1841_F11_7_red_green.jpg)
![](https://images.proteinatlas.org/4195/1841_F11_8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13761-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
