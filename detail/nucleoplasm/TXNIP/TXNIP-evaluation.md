---
type: protein-evaluation
gene: "TXNIP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TXNIP — REJECTED (研究热度过高 (PubMed strict=1857，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TXNIP / VDUP1 |
| 蛋白名称 | Thioredoxin-interacting protein |
| 蛋白大小 | 391 aa / 43.7 kDa |
| UniProt ID | Q9H3M7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 391 aa / 43.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1857 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.7; PDB: 4GEI, 4GEJ, 4GFX, 4LL1, 4LL4, 4ROF, 4ROJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014752, IPR011021, IPR011022, IPR050357, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1857 |
| PubMed broad count | 2424 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: VDUP1 |

**关键文献**:
1. TXNIP: A key protein in the cellular stress response pathway and a potential therapeutic target.. *Experimental & molecular medicine*. PMID: 37394581
2. D-mannose alleviates intervertebral disc degeneration through glutamine metabolism.. *Military Medical Research*. PMID: 38711073
3. Thioredoxin-interacting protein links oxidative stress to inflammasome activation.. *Nature immunology*. PMID: 20023662
4. TXNIP Suppresses the Osteochondrogenic Switch of Vascular Smooth Muscle Cells in Atherosclerosis.. *Circulation research*. PMID: 36448450
5. FOXO regulation of TXNIP induces ferroptosis in satellite cells by inhibiting glutathione metabolism, promoting Sarcopenia.. *Cellular and molecular life sciences : CMLS*. PMID: 39982519

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.7 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 26.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 73.4% |
| 可用 PDB 条目 | 4GEI, 4GEJ, 4GFX, 4LL1, 4LL4, 4ROF, 4ROJ, 5CQ2, 5DF6, 5DWS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4GEI, 4GEJ, 4GFX, 4LL1, 4LL4, 4ROF, 4ROJ, 5CQ2, 5DF6, 5DWS）+ AlphaFold极高置信度预测（pLDDT=78.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014752, IPR011021, IPR011022, IPR050357, IPR014756; Pfam: PF02752, PF00339 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NLRP3 | 0.999 | 0.510 | — |
| TXN2 | 0.999 | 0.331 | — |
| TXN | 0.999 | 0.991 | — |
| DDIT4 | 0.991 | 0.292 | — |
| ITCH | 0.989 | 0.983 | — |
| PTPN11 | 0.972 | 0.971 | — |
| VAV2 | 0.950 | 0.946 | — |
| CASP1 | 0.867 | 0.000 | — |
| HMOX1 | 0.859 | 0.000 | — |
| TP53 | 0.855 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pif1A | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Vdup1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PSMG1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| deoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| clpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| TXN | psi-mi:"MI:0018"(two hybrid) | pubmed:10814541 |
| Dmel\CG46385 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| glpC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NLGN3 | psi-mi:"MI:0018"(two hybrid) | pubmed:25464930|imex:IM-26157 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.7 + PDB: 4GEI, 4GEJ, 4GFX, 4LL1, 4LL4,  | pLDDT=78.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Plasma membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TXNIP — Thioredoxin-interacting protein，研究基础较多，新颖性有限。
2. 蛋白大小391 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1857 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1857 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3M7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000265972-TXNIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TXNIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3M7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000265972-TXNIP/subcellular

![](https://images.proteinatlas.org/53694/904_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/53694/904_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3M7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
