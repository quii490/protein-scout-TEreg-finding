---
type: protein-evaluation
gene: "MYD88"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MYD88 — REJECTED (研究热度过高 (PubMed strict=7119，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYD88 |
| 蛋白名称 | Myeloid differentiation primary response protein MyD88 |
| 蛋白大小 | 296 aa / 33.2 kDa |
| UniProt ID | Q99836 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Vesicles, Mitochondria; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 296 aa / 33.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=7119 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.6; PDB: 2JS7, 2Z5V, 3MOP, 4DOM, 4EO7, 6I3N, 7BEQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011029, IPR000488, IPR034249, IPR017281, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles, Mitochondria | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- extrinsic component of cytoplasmic side of plasma membrane (GO:0031234)
- extrinsic component of plasma membrane (GO:0019897)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7119 |
| PubMed broad count | 13738 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MyD88 mediates colorectal cancer cell proliferation, migration and invasion via NF‑κB/AP‑1 signaling pathway.. *International journal of molecular medicine*. PMID: 31746347
2. MyD88 in Mycobacterium tuberculosis infection.. *Medical microbiology and immunology*. PMID: 28220253
3. Macroglobulinemia and Autoinflammatory Disease.. *Rheumatology and immunology research*. PMID: 36467983
4. MyD88 and Its Inhibitors in Cancer: Prospects and Challenges.. *Biomolecules*. PMID: 38785969
5. Toll-like receptor mediated inflammation requires FASN-dependent MYD88 palmitoylation.. *Nature chemical biology*. PMID: 31427815

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.6 |
| 高置信度残基 (pLDDT>90) 占比 | 13.9% |
| 置信残基 (pLDDT 70-90) 占比 | 69.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 2JS7, 2Z5V, 3MOP, 4DOM, 4EO7, 6I3N, 7BEQ, 7BER, 7L6W, 8S78 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2JS7, 2Z5V, 3MOP, 4DOM, 4EO7, 6I3N, 7BEQ, 7BER, 7L6W, 8S78）+ AlphaFold极高置信度预测（pLDDT=80.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011029, IPR000488, IPR034249, IPR017281, IPR000157; Pfam: PF00531, PF13676 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LY96 | 0.999 | 0.000 | — |
| IRF7 | 0.999 | 0.585 | — |
| TLR4 | 0.999 | 0.974 | — |
| TLR3 | 0.999 | 0.435 | — |
| TLR8 | 0.999 | 0.236 | — |
| TLR5 | 0.999 | 0.555 | — |
| TIRAP | 0.999 | 0.848 | — |
| MAP3K7 | 0.999 | 0.960 | — |
| IRAK2 | 0.999 | 0.975 | — |
| IKBKG | 0.999 | 0.994 | — |

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
| 三维结构 | AlphaFold pLDDT=80.6 + PDB: 2JS7, 2Z5V, 3MOP, 4DOM, 4EO7,  | pLDDT=80.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Vesicles, Mitochondria | 一致 |
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
1. MYD88 — Myeloid differentiation primary response protein MyD88，研究基础较多，新颖性有限。
2. 蛋白大小296 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7119 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 7119 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99836
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172936-MYD88/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYD88
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99836
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000172936-MYD88/subcellular

![](https://images.proteinatlas.org/9104/1432_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9104/1432_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9104/954_E1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/9104/954_E1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/9104/956_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9104/956_E1_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99836-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99836 |
| SMART | SM00005;SM00255; |
| UniProt Domain [FT] | DOMAIN 54..109; /note="Death"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00064"; DOMAIN 159..293; /note="TIR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00204" |
| InterPro | IPR011029;IPR000488;IPR034249;IPR017281;IPR000157;IPR035897; |
| Pfam | PF00531;PF13676; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172936-MYD88/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC6 | Intact, Biogrid | true |
| IRAK1 | Intact, Biogrid | true |
| IRAK4 | Intact, Biogrid | true |
| SIAH1 | Intact, Biogrid | true |
| SMAD3 | Intact, Biogrid | true |
| SPOP | Intact, Biogrid | true |
| STAP2 | Intact, Biogrid | true |
| TIRAP | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
