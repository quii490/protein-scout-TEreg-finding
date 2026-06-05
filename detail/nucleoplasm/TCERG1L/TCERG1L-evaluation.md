---
type: protein-evaluation
gene: "TCERG1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCERG1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCERG1L |
| 蛋白名称 | Transcription elongation regulator 1-like protein |
| 蛋白大小 | 586 aa / 65.7 kDa |
| UniProt ID | Q5VWI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 586 aa / 65.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002713, IPR036517, IPR045148, IPR001202, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DNA methylation biomarker candidates for early detection of colon cancer.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 22238052
2. Genetic and functional evidence for a locus controlling otitis media at chromosome 10q26.3.. *BMC medical genetics*. PMID: 24499112
3. Roles of Stra8 and Tcerg1l in retinoic acid induced spermatogonial differentiation in mouse†.. *Biology of reproduction*. PMID: 33959758
4. Genome-wide differential methylation analyses identifies methylation signatures of male infertility.. *Human reproduction (Oxford, England)*. PMID: 30358834
5. Detection of DNA hypermethylation in sera of patients with Crohn's disease.. *Molecular medicine reports*. PMID: 24317008

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 58.2% |
| 有序区域 (pLDDT>70) 占比 | 31.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.5），有序残基占 31.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002713, IPR036517, IPR045148, IPR001202, IPR036020; Pfam: PF01846, PF23517 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDX46 | 0.905 | 0.840 | — |
| MFAP1 | 0.892 | 0.840 | — |
| PRPF38A | 0.869 | 0.840 | — |
| SF3B1 | 0.858 | 0.840 | — |
| RBM22 | 0.856 | 0.840 | — |
| SNRPA1 | 0.852 | 0.840 | — |
| SNW1 | 0.846 | 0.840 | — |
| SF3A3 | 0.845 | 0.840 | — |
| PRPF19 | 0.845 | 0.840 | — |
| SF3A1 | 0.844 | 0.840 | — |

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
| 三维结构 | AlphaFold pLDDT=57.5 + PDB: 无 | pLDDT=57.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TCERG1L — Transcription elongation regulator 1-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小586 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VWI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176769-TCERG1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCERG1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VWI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000176769-TCERG1L/subcellular

![](https://images.proteinatlas.org/30816/1969_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/30816/1969_B1_4_red_green.jpg)
![](https://images.proteinatlas.org/30816/330_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/30816/330_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/30816/331_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/30816/331_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VWI1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
