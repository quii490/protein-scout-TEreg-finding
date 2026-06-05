---
type: protein-evaluation
gene: "VPS13D"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS13D 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS13D / KIAA0453 |
| 蛋白名称 | Intermembrane lipid transfer protein VPS13D |
| 蛋白大小 | 4388 aa / 491.9 kDa |
| UniProt ID | Q5THJ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 0/10 | ×1 | 0 | 4388 aa / 491.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015940, IPR009060, IPR041969, IPR026847, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0453 |

**关键文献**:
1. VPS13D Movement Disorder.. **. PMID: 30789691
2. Microglia promote inflammatory cell death upon neuronal mitochondrial impairment during neurodegeneration.. *Nature structural & molecular biology*. PMID: 40563011
3. VPS13D bridges the ER to mitochondria and peroxisomes via Miro.. *The Journal of cell biology*. PMID: 33891013
4. VPS13D promotes peroxisome biogenesis.. *The Journal of cell biology*. PMID: 33891012
5. VPS13D mutations affect mitochondrial homeostasis and locomotion in Caenorhabditis elegans.. *G3 (Bethesda, Md.)*. PMID: 39957248

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015940, IPR009060, IPR041969, IPR026847, IPR056747; Pfam: PF25033, PF12624, PF25036 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATG2B | 0.814 | 0.000 | — |
| RHOT1 | 0.628 | 0.000 | — |
| VPS13B | 0.573 | 0.000 | — |
| VPS13A | 0.556 | 0.000 | — |
| PLIN5 | 0.521 | 0.000 | — |
| KIAA2013 | 0.488 | 0.000 | — |
| ZZEF1 | 0.485 | 0.000 | — |
| MIGA2 | 0.483 | 0.000 | — |
| VPS13C | 0.462 | 0.000 | — |
| TSG101 | 0.451 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MADD | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| Q81Y62 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| J3KP14 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13780|pubmed:21182205 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. VPS13D — Intermembrane lipid transfer protein VPS13D，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小4388 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5THJ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000048707-VPS13D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS13D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5THJ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000048707-VPS13D/subcellular

![](https://images.proteinatlas.org/27332/1486_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/27332/1486_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/27332/1496_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/27332/1496_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/27332/1551_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/27332/1551_H9_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
