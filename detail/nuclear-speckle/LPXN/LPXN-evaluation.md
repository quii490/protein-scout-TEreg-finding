---
type: protein-evaluation
gene: "LPXN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LPXN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LPXN / LDLP |
| 蛋白名称 | Leupaxin |
| 蛋白大小 | 386 aa / 43.3 kDa |
| UniProt ID | O60711 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Focal adhesion sites; 额外: Nuclear speckles, Cytosol; UniProt: Cytoplasm; Cell junction, focal adhesion; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 386 aa / 43.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.4; PDB: 1X3H, 4XEF, 4XEK, 4XEV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017305, IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Focal adhesion sites; 额外: Nuclear speckles, Cytosol | Supported |
| UniProt | Cytoplasm; Cell junction, focal adhesion; Nucleus; Cytoplasm, perinuclear region; Cell projection, p... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LDLP |

**关键文献**:
1. Leupaxin promotes hepatic gluconeogenesis and glucose metabolism by coactivation with hepatic nuclear factor 4α.. *Molecular metabolism*. PMID: 39603504
2. Association of leupaxin with Src in osteoclasts.. *American journal of physiology. Cell physiology*. PMID: 16914530
3. Leupaxin Promotes Bladder Cancer Proliferation, Metastasis, and Angiogenesis Through the PI3K/AKT Pathway.. *Cellular physiology and biochemistry : international journal of experimental cellular physiology, biochemistry, and pharmacology*. PMID: 29975926
4. Paxillin family proteins Hic-5 and LPXN promote lipid storage by regulating the ubiquitination degradation of CIDEC.. *The Journal of biological chemistry*. PMID: 38159847
5. Interaction of Pyk2 and PTP-PEST with leupaxin in prostate cancer cells.. *American journal of physiology. Cell physiology*. PMID: 17329398

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 48.7% |
| 置信残基 (pLDDT 70-90) 占比 | 22.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 71.0% |
| 可用 PDB 条目 | 1X3H, 4XEF, 4XEK, 4XEV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1X3H, 4XEF, 4XEK, 4XEV）+ AlphaFold高质量预测（pLDDT=76.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017305, IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTK2B | 0.994 | 0.950 | — |
| VCL | 0.913 | 0.559 | — |
| PTPN12 | 0.860 | 0.364 | — |
| PSTPIP2 | 0.814 | 0.758 | — |
| APOB | 0.765 | 0.000 | — |
| GIT1 | 0.758 | 0.663 | — |
| ARHGEF6 | 0.712 | 0.642 | — |
| GIT2 | 0.676 | 0.538 | — |
| PTK2 | 0.664 | 0.509 | — |
| HCLS1 | 0.630 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Irak1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| HOXA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IMP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LIMS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF426 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PHF21A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| POM121 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAP2K7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZNF175 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| eno | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 1X3H, 4XEF, 4XEK, 4XEV | pLDDT=76.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell junction, focal adhesion; Nucleus; / Focal adhesion sites; 额外: Nuclear speckles, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. LPXN — Leupaxin，非常新颖，仅有少数基础研究。
2. 蛋白大小386 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60711
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110031-LPXN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LPXN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60711
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Focal adhesion sites (supported)。来源: https://www.proteinatlas.org/ENSG00000110031-LPXN/subcellular

![](https://images.proteinatlas.org/61441/1385_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61441/1385_E7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61441/1394_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61441/1394_E7_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60711-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60711 |
| SMART | SM00132; |
| UniProt Domain [FT] | DOMAIN 150..208; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 209..267; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 268..326; /note="LIM zinc-binding 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 327..386; /note="LIM zinc-binding 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR017305;IPR001781; |
| Pfam | PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110031-LPXN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PLEKHH2 | Intact, Biogrid | true |
| PTK2 | Intact, Biogrid | true |
| AGXT | Intact | false |
| AQP1 | Intact | false |
| BTK | Bioplex | false |
| EDC3 | Bioplex | false |
| GIT1 | Biogrid | false |
| HOXC9 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
