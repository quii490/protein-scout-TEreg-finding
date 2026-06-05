---
type: protein-evaluation
gene: "MEN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MEN1 — REJECTED (研究热度过高 (PubMed strict=1702，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEN1 / SCG2 |
| 蛋白名称 | Menin |
| 蛋白大小 | 610 aa / 67.5 kDa |
| UniProt ID | O00255 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 610 aa / 67.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1702 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.4; PDB: 3U84, 3U85, 3U86, 3U88, 4GPQ, 4GQ3, 4GQ4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007747; Pfam: PF05053 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- cleavage furrow (GO:0032154)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum lumen (GO:0005788)
- histone methyltransferase complex (GO:0035097)
- MLL1 complex (GO:0071339)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1702 |
| PubMed broad count | 3453 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCG2 |

**关键文献**:
1. Multiple endocrine neoplasia type 1 (MEN1): recommendations and guidelines for best practice.. *The lancet. Diabetes & endocrinology*. PMID: 40523372
2. Clinical practice guidelines for multiple endocrine neoplasia type 1 (MEN1).. *The Journal of clinical endocrinology and metabolism*. PMID: 22723327
3. Menin in Cancer.. *Genes*. PMID: 39336822
4. Familial pituitary tumors.. *Handbook of clinical neurology*. PMID: 25248598
5. [Multiple Endocrine Neoplasia].. *Gan to kagaku ryoho. Cancer & chemotherapy*. PMID: 31296813

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.4 |
| 高置信度残基 (pLDDT>90) 占比 | 72.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 19.7% |
| 有序区域 (pLDDT>70) 占比 | 78.5% |
| 可用 PDB 条目 | 3U84, 3U85, 3U86, 3U88, 4GPQ, 4GQ3, 4GQ4, 4GQ6, 4I80, 4OG3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3U84, 3U85, 3U86, 3U88, 4GPQ, 4GQ3, 4GQ4, 4GQ6, 4I80, 4OG3）+ AlphaFold极高置信度预测（pLDDT=84.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007747; Pfam: PF05053 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SF1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:26420826|imex:IM-23671 |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM23 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| E2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18305892|imex:IM-19324 |
| ESR1 | psi-mi:"MI:0096"(pull down) | imex:IM-13781|pubmed:21182203 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.4 + PDB: 3U84, 3U85, 3U86, 3U88, 4GPQ,  | pLDDT=84.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

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
1. MEN1 — Menin，研究基础较多，新颖性有限。
2. 蛋白大小610 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1702 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1702 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00255
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133895-MEN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00255
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000133895-MEN1/subcellular

![](https://images.proteinatlas.org/30342/295_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/30342/295_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/30342/296_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/30342/296_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/30342/297_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/30342/297_A11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00255-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
