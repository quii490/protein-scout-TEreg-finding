---
type: protein-evaluation
gene: "DIO2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DIO2 — REJECTED (研究热度过高 (PubMed strict=659，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIO2 / ITDI2, TXDI2 |
| 蛋白名称 | Type II iodothyronine deiodinase |
| 蛋白大小 | 273 aa / 30.6 kDa |
| UniProt ID | Q92813 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; 额外: Plasma membrane; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 30.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=659 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000643, IPR008261, IPR036249; Pfam: PF00837 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Plasma membrane | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 659 |
| PubMed broad count | 1023 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ITDI2, TXDI2 |

**关键文献**:
1. Defective autophagy contributes to endometrial epithelial-mesenchymal transition in intrauterine adhesions.. *Autophagy*. PMID: 35196191
2. Comparative Effectiveness of Levothyroxine, Desiccated Thyroid Extract, and Levothyroxine+Liothyronine in Hypothyroidism.. *The Journal of clinical endocrinology and metabolism*. PMID: 34185829
3. Adipocyte RNA-binding protein CELF1 promotes beiging of white fat through stabilizing Dio2 mRNA.. *Nature communications*. PMID: 40789858
4. Combined deletion of Mct8 and Dio2 impairs SVZ neurogliogenesis and olfactory function in adult mice.. *Neurobiology of disease*. PMID: 38901782
5. Local DIO2 Elevation Is an Adaption in Malformed Cerebrovasculature.. *Circulation research*. PMID: 40130314

**评价**: 研究基础较多，新颖性有限。

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
| InterPro/Pfam | InterPro: IPR000643, IPR008261, IPR036249; Pfam: PF00837 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DIO1 | 0.934 | 0.000 | — |
| SECISBP2 | 0.916 | 0.000 | — |
| SLC16A2 | 0.897 | 0.000 | — |
| WSB1 | 0.856 | 0.651 | — |
| UCP1 | 0.849 | 0.000 | — |
| TRH | 0.845 | 0.000 | — |
| GPBAR1 | 0.834 | 0.000 | — |
| CIDEA | 0.808 | 0.000 | — |
| SLCO1C1 | 0.804 | 0.000 | — |
| TSHB | 0.786 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm, Vesicles; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DIO2 — Type II iodothyronine deiodinase，研究基础较多，新颖性有限。
2. 蛋白大小273 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 659 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 659 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92813
- Protein Atlas: https://www.proteinatlas.org/ENSG00000211448-DIO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92813
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000211448-DIO2/subcellular

![](https://images.proteinatlas.org/48002/740_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/48002/740_C8_5_red_green.jpg)
![](https://images.proteinatlas.org/48002/784_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/48002/784_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/48002/990_B11_6_red_green.jpg)
![](https://images.proteinatlas.org/48002/990_B11_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
