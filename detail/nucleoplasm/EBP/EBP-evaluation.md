---
type: protein-evaluation
gene: "EBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EBP — REJECTED (研究热度过高 (PubMed strict=6580，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EBP |
| 蛋白名称 | 3-beta-hydroxysteroid-Delta(8),Delta(7)-isomerase |
| 蛋白大小 | 230 aa / 26.4 kDa |
| UniProt ID | Q15125 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus envelope; Cytoplasmi |
| 蛋白大小 | 10/10 | ×1 | 10 | 230 aa / 26.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6580 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.6; PDB: 6OHT, 6OHU, 8W0R, 8W0S |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007905, IPR033118; Pfam: PF05241 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Nucleus envelope; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear envelope (GO:0005635)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6580 |
| PubMed broad count | 11753 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CCAAT enhancer binding protein gamma (C/EBP-γ): An understudied transcription factor.. *Advances in biological regulation*. PMID: 35121409
2. The methylation of C/EBP β gene promoter and regulated by GATA-2 protein.. *Molecular biology reports*. PMID: 23065276
3. Interleukin-6 regulates human ODAM gene expression in gingival epithelial cells.. *Journal of periodontal & implant science*. PMID: 40350767
4. Lipopolysaccharide induces 5-lipoxygenase-activating protein gene expression in THP-1 cells via a NF-kappaB and C/EBP-mediated mechanism.. *American journal of physiology. Cell physiology*. PMID: 15625306
5. CCAAT/enhancer-binding proteins and the pathogenesis of retrovirus infection.. *Future microbiology*. PMID: 19327116

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 92.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 96.5% |
| 可用 PDB 条目 | 6OHT, 6OHU, 8W0R, 8W0S |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6OHT, 6OHU, 8W0R, 8W0S）+ AlphaFold高质量预测（pLDDT=95.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007905, IPR033118; Pfam: PF05241 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SC5D | 0.995 | 0.000 | — |
| TM7SF2 | 0.991 | 0.000 | — |
| DHCR24 | 0.981 | 0.238 | — |
| DHCR7 | 0.966 | 0.000 | — |
| NSDHL | 0.964 | 0.000 | — |
| HSD17B7 | 0.961 | 0.000 | — |
| KCNH6 | 0.901 | 0.000 | — |
| ARSL | 0.837 | 0.000 | — |
| FADS1 | 0.833 | 0.000 | — |
| FDFT1 | 0.783 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 6OHT, 6OHU, 8W0R, 8W0S | pLDDT=95.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus envelope;  / Nuclear membrane, Endoplasmic reticulum | 一致 |
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
1. EBP — 3-beta-hydroxysteroid-Delta(8),Delta(7)-isomerase，研究基础较多，新颖性有限。
2. 蛋白大小230 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6580 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6580 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15125
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147155-EBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15125
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000147155-EBP/subcellular

![](https://images.proteinatlas.org/3130/2074_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3130/2074_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3130/56_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3130/56_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3130/57_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3130/57_D4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15125-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15125 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 61..204; /note="EXPERA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01087" |
| InterPro | IPR007905;IPR033118; |
| Pfam | PF05241; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147155-EBP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABHD16A | Intact | false |
| ACTA1 | Bioplex | false |
| APP | Biogrid | false |
| AQP6 | Intact | false |
| ARL13B | Intact | false |
| ARL6IP6 | Intact | false |
| ARV1 | Intact | false |
| BMP10 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
