---
type: protein-evaluation
gene: "NUP37"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUP37 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUP37 |
| 蛋白名称 | Nucleoporin Nup37 |
| 蛋白大小 | 326 aa / 36.7 kDa |
| UniProt ID | Q8NFH4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Chromosome, centromere, kinetochore; Nucleus, nuclear pore c |
| 蛋白大小 | 10/10 | ×1 | 10 | 326 aa / 36.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.5; PDB: 5A9Q, 7PEQ, 7R5J, 7R5K |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037626, IPR015943, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.5/180** | |
| **归一化总分** | | | **73.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Chromosome, centromere, kinetochore; Nucleus, nuclear pore complex | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- nuclear envelope (GO:0005635)
- nuclear pore (GO:0005643)
- nuclear pore outer ring (GO:0031080)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. NUP37 accumulation mediated by TRIM28 enhances lipid synthesis to accelerate HCC progression.. *Oncogene*. PMID: 39294431
2. Deletion of low-density lipoprotein-related receptor 5 inhibits liver Cancer cell proliferation via destabilizing Nucleoporin 37.. *Cell communication and signaling : CCS*. PMID: 31881970
3. NUP37 promotes the proliferation and invasion of glioma cells through DNMT1-mediated methylation.. *Cell death discovery*. PMID: 39174498
4. Nucleoporin37 may play a role in early embryo development in human and mice.. *Molecular human reproduction*. PMID: 35583302
5. Demethylation at enhancer upregulates MCM2 and NUP37 expression predicting poor survival in hepatocellular carcinoma patients.. *Journal of translational medicine*. PMID: 35093119

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.5 |
| 高置信度残基 (pLDDT>90) 占比 | 84.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 94.8% |
| 可用 PDB 条目 | 5A9Q, 7PEQ, 7R5J, 7R5K |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5A9Q, 7PEQ, 7R5J, 7R5K）+ AlphaFold高质量预测（pLDDT=92.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037626, IPR015943, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEH1L | 0.999 | 0.910 | — |
| NUP133 | 0.999 | 0.998 | — |
| NUP43 | 0.999 | 0.998 | — |
| NUP98 | 0.999 | 0.884 | — |
| AHCTF1 | 0.999 | 0.948 | — |
| NUP107 | 0.999 | 0.998 | — |
| NUP160 | 0.999 | 0.953 | — |
| NUP85 | 0.999 | 0.998 | — |
| SEC13 | 0.999 | 0.998 | — |
| NUP35 | 0.990 | 0.811 | — |

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
| 三维结构 | AlphaFold pLDDT=92.5 + PDB: 5A9Q, 7PEQ, 7R5J, 7R5K | pLDDT=92.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome, centromere, kinetochore; Nucleus, nucl / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NUP37 — Nucleoporin Nup37，非常新颖，仅有少数基础研究。
2. 蛋白大小326 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFH4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075188-NUP37/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUP37
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFH4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000075188-NUP37/subcellular

![](https://images.proteinatlas.org/56300/913_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/56300/913_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/56300/914_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/56300/914_G5_5_red_green.jpg)
![](https://images.proteinatlas.org/56300/919_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/56300/919_G5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFH4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
