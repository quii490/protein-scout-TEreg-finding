---
type: protein-evaluation
gene: "NMRAL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NMRAL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NMRAL1 / HSCARG |
| 蛋白名称 | NmrA-like family domain-containing protein 1 |
| 蛋白大小 | 299 aa / 33.3 kDa |
| UniProt ID | Q9HBL8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 299 aa / 33.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.6; PDB: 2EXX, 2WM3, 2WMD, 3DXF, 3E5M |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036291, IPR008030, IPR051164; Pfam: PF05368 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HSCARG |

**关键文献**:
1. Integration of summary data from GWAS and eQTL studies predicts complex trait gene targets.. *Nature genetics*. PMID: 27019110
2. Colon mucosal proteomics of ankylosing spondylitis versus gut inflammation.. *PloS one*. PMID: 39671362
3. Functional variant rs2270363 on 16p13.3 confers schizophrenia risk by regulating NMRAL1.. *Brain : a journal of neurology*. PMID: 35094059
4. Structure and functions of cellular redox sensor HSCARG/NMRAL1, a linkage among redox status, innate immunity, DNA damage response, and cancer.. *Free radical biology & medicine*. PMID: 32950687
5. NMRAL1 as a Causal Factor in Postherpetic Neuralgia: A Proteome-Wide Mendelian Randomization Study.. *Journal of pain research*. PMID: 40438617

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.6 |
| 高置信度残基 (pLDDT>90) 占比 | 96.7% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 99.4% |
| 可用 PDB 条目 | 2EXX, 2WM3, 2WMD, 3DXF, 3E5M |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2EXX, 2WM3, 2WMD, 3DXF, 3E5M）+ AlphaFold极高置信度预测（pLDDT=96.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036291, IPR008030, IPR051164; Pfam: PF05368 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFS3 | 0.874 | 0.571 | — |
| UQCRFS1 | 0.861 | 0.557 | — |
| CYC1 | 0.849 | 0.567 | — |
| NDUFV1 | 0.845 | 0.571 | — |
| ASS1 | 0.845 | 0.292 | — |
| NDUFA8 | 0.832 | 0.575 | — |
| NDUFS8 | 0.830 | 0.571 | — |
| NDUFS2 | 0.826 | 0.571 | — |
| NDUFA12 | 0.815 | 0.571 | — |
| USP7 | 0.811 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FOXJ1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-2845884 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| aguA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PHB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Hmga2 | psi-mi:"MI:0096"(pull down) | imex:IM-23312|pubmed:26045162 |
| Agap2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28706196|doi:10.1038/s4 |
| OPTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACTA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GALNT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.6 + PDB: 2EXX, 2WM3, 2WMD, 3DXF, 3E5M | pLDDT=96.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NMRAL1 — NmrA-like family domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小299 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBL8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153406-NMRAL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NMRAL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBL8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000153406-NMRAL1/subcellular

![](https://images.proteinatlas.org/41353/1208_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/41353/1208_F2_5_red_green.jpg)
![](https://images.proteinatlas.org/62287/1106_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/62287/1106_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/62287/1148_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/62287/1148_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HBL8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HBL8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036291;IPR008030;IPR051164; |
| Pfam | PF05368; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153406-NMRAL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSPA8 | Biogrid, Bioplex | true |
| ACTA1 | Bioplex | false |
| ASS1 | Intact | false |
| GALNT1 | Bioplex | false |
| OPTN | Intact | false |
| OTUB2 | Biogrid | false |
| PCNA | Biogrid | false |
| PHB2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
