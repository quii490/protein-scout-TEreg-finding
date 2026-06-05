---
type: protein-evaluation
gene: "NFKBIB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NFKBIB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFKBIB / IKBB, TRIP9 |
| 蛋白名称 | NF-kappa-B inhibitor beta |
| 蛋白大小 | 356 aa / 37.8 kDa |
| UniProt ID | Q15653 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 356 aa / 37.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.4; PDB: 9CK0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IKBB, TRIP9 |

**关键文献**:
1. Discovering new hub genes of dilated cardiomyopathy.. *ESC heart failure*. PMID: 40074718
2. Dipeptidyl peptidase 9 (DPP9) depletion from hepatocytes in experimental primary liver cancer.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 40187163
3. Nuclear KIT induces a NFKBIB-RELA-KIT autoregulatory loop in imatinib-resistant gastrointestinal stromal tumors.. *Oncogene*. PMID: 31363162
4. IkappaB genetic polymorphisms and invasive pneumococcal disease.. *American journal of respiratory and critical care medicine*. PMID: 17463416
5. Differential expression of genes regulated by the glucocorticoid receptor pathway in patients with pulmonary tuberculosis.. *Life sciences*. PMID: 35526591

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 56.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 27.0% |
| 有序区域 (pLDDT>70) 占比 | 61.2% |
| 可用 PDB 条目 | 9CK0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.4，有序区 61.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REL | 0.999 | 0.887 | — |
| NFKBIA | 0.999 | 0.832 | — |
| RELA | 0.999 | 0.948 | — |
| NFKB1 | 0.998 | 0.858 | — |
| CHUK | 0.997 | 0.794 | — |
| IKBKB | 0.997 | 0.777 | — |
| IKBKG | 0.994 | 0.631 | — |
| NFKBIE | 0.993 | 0.000 | — |
| RELB | 0.993 | 0.497 | — |
| BTRC | 0.983 | 0.618 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000489138.1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| Rela | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| POLR1G | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| FBXW11 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| REL | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| CHUK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 9CK0 | pLDDT=76.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NFKBIB — NF-kappa-B inhibitor beta，非常新颖，仅有少数基础研究。
2. 蛋白大小356 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15653
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104825-NFKBIB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFKBIB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15653
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104825-NFKBIB/subcellular

![](https://images.proteinatlas.org/63734/1139_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/63734/1139_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/63734/1254_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/63734/1254_E5_9_red_green.jpg)
![](https://images.proteinatlas.org/63734/2104_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/63734/2104_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15653-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
