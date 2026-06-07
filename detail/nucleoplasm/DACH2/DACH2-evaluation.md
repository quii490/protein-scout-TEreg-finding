---
type: protein-evaluation
gene: "DACH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DACH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DACH2 |
| 蛋白名称 | Dachshund homolog 2 |
| 蛋白大小 | 599 aa / 65.3 kDa |
| UniProt ID | Q96NX9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 599 aa / 65.3 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052417, IPR009061, IPR003380, IPR037000; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 44 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Dach2-Hdac9 signaling regulates reinnervation of muscle endplates.. *Development (Cambridge, England)*. PMID: 26483211
2. Mouse Dach1 and Dach2 are redundantly required for Müllerian duct development.. *Genesis (New York, N.Y. : 2000)*. PMID: 18395837
3. Mouse Dach2 mutants do not exhibit gross defects in eye development or brain function.. *Genesis (New York, N.Y. : 2000)*. PMID: 16470613
4. Characterization of mouse Dach2, a homologue of Drosophila dachshund.. *Mechanisms of development*. PMID: 11287190
5. Discovery of dachshund 2 protein as a novel biomarker of poor prognosis in epithelial ovarian cancer.. *Journal of ovarian research*. PMID: 22284433

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 29.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 51.8% |
| 有序区域 (pLDDT>70) 占比 | 37.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 37.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052417, IPR009061, IPR003380, IPR037000; Pfam: PF02437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DACH1 | 0.847 | 0.757 | — |
| EYA2 | 0.800 | 0.300 | — |
| IL1RAPL2 | 0.697 | 0.051 | — |
| POF1B | 0.680 | 0.000 | — |
| SATL1 | 0.609 | 0.069 | — |
| EYA1 | 0.586 | 0.300 | — |
| HDAC9 | 0.585 | 0.045 | — |
| KLHL4 | 0.574 | 0.067 | — |
| DIAPH2 | 0.568 | 0.000 | — |
| MYOG | 0.532 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 无 | pLDDT=61.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DACH2 -- Dachshund homolog 2，非常新颖，仅有少数基础研究。
2. 蛋白大小599 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96NX9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126733-DACH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DACH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NX9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DACH2/IF_images/DACH2_A_431_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DACH2/IF_images/DACH2_A_431_1.jpg]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000126733-DACH2/subcellular

![](https://images.proteinatlas.org/1367/170_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/1367/170_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/1367/171_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/1367/171_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/1367/1851_D3_31_red_green.jpg)
![](https://images.proteinatlas.org/1367/1851_D3_32_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96NX9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96NX9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052417;IPR009061;IPR003380;IPR037000; |
| Pfam | PF02437; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000126733-DACH2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
