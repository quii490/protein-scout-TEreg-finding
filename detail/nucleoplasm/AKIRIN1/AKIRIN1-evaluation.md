---
type: protein-evaluation
gene: "AKIRIN1"
date: 2026-06-04
tags: [protein-scout, rescored, rescued-to-scored, critical-false-rejection]
status: rescored-to-scored
previous_status: scored
previous_rejection_reason: nuclear_score ≤ 3
rescue_reason: "HPA Nucleoplasm+Nuclear membrane(Approved); GO-CC chromatin(IBA)+nucleoplasm(IDA:HPA); UniProt Nucleus(IDA); 极度新颖(16篇); nuclear_score=3显著低估"
revised_nuclear_score: 7
---

## AKIRIN1 核蛋白评估报告 -- CRITICAL FALSE REJECTION RE-EVALUATION

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKIRIN1 / C1orf108 |
| 蛋白大小 | 192 aa / 21.9 kDa |
| UniProt ID | Q9H9L7 |
| 蛋白全名 | Akirin-1 |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Nuclear membrane |
| HPA Reliability | Approved |
| 原评估状态 | REJECTED (nuclear_score=3) |
| 重新评估日期 | 2026-06-04 |
| 重新评估结果 | **RESCUED TO SCORED** |

### 2. 评分总览（修订后）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **7/10** | ×4 | 28 | HPA Nucleoplasm+Nuclear membrane(Approved); GO-CC chromatin+nucleoplasm; UniProt Nucleus(IDA) |
| 蛋白大小 | 5/10 | ×1 | 5 | 192aa/21.9kDa，极小蛋白但含adaptor功能 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | pLDDT=68.1, pct<50=27.1%，高比例无序 |
| 调控结构域 | 4/10 | ×2 | 8 | IPR024132 (Akirin family)，adaptor蛋白，无经典DNA结合域 |
| PPI网络 | 6/10 | ×3 | 18 | STRING: AKIRIN2(0.849实验), PSMA5/PSMB3(实验); 蛋白酶体+核转运 |
| **加权总分** | | | **121/180** | |
| **归一化总分 (÷1.8)** | | | **67.2/100** | |

### 3. False rejection recheck -- CRITICAL

**为何本次重新评估被列为CRITICAL:**

AKIRIN1代表了"核定位极其明确但蛋白过小+结构无序导致综合评分偏低而错误拒绝"的典型。GO-CC含chromatin注释(IBA)，这在所有评估基因中极为罕见——直接暗示染色质相互作用。HPA Approved最高可信度的Nucleoplasm+Nuclear membrane双定位也是最佳核定位证据之一。

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet)**:
   - Nucleus: ECO:0000269 (IDA, 实验验证)
   - 单一核定位，无胞质注释

2. **GO-CC (harvest packet) -- 极为丰富的核注释**:
   - GO:0000785 chromatin: IBA:GO_Central -- **罕见的染色质注释!**
   - GO:0031965 nuclear membrane: IDA:HPA (实验)
   - GO:0005654 nucleoplasm: IDA:HPA (实验)
   - GO:0005634 nucleus: IDA:UniProtKB (实验)
   - **四个核GO术语，含染色质，在10个CRITICAL基因中独一无二**

3. **HPA Subcellular (harvest packet)**:
   - Main location: Nucleoplasm
   - Additional: Nuclear membrane
   - Reliability: Approved (最高可信度)
   - 纯核定位，无胞质/膜信号

4. **功能证据**:
   - 作为分子adaptor桥接蛋白间相互作用
   - 参与骨骼肌发育(通过PI3K通路调控actin骨架)
   - 与AKIRIN2不同，不参与蛋白酶体核转运
   - 在天然杀伤细胞和粒细胞中作为参考基因

**为何原核定位评分=3是错误的:**

AKIRIN1同时拥有:
- HPA Approved Nucleoplasm+Nuclear membrane (纯核定位)
- GO-CC chromatin (IBA, 暗示染色质结合)
- UniProt Nucleus (IDA实验)
- 无任何胞质注释(GO-CC胞质条目为0)

这组核定位证据在研究基因中属于最高水平。chromatin的IBA注释虽然有别于IDA，但来自GO_Central的进化保守推断仍有较高可信度。核定位评分至少应为7/10。

**修订后核定位评分: 7/10**
- HPA Approved纯核定位: 核蛋白确认
- GO-CC chromatin: 暗示功能核定位(染色质关联)
- UniProt Nucleus IDA: 独立实验验证
- 扣分项: chromatin为IBA(推断)而非IDA; AlphaFold结构无序(但结构质量与核定位证据独立)
- 加分项: 纯核定位，无胞质contamination

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | Nucleoplasm (main) | Approved (最高) | IF实验 |
| HPA (IF) | Nuclear membrane (additional) | Approved (最高) | IF实验 |
| UniProt | Nucleus | IDA | ECO:0000269 |
| GO-CC | chromatin | IBA:GO_Central | 进化保守推断 |
| GO-CC | nuclear membrane | IDA:HPA | 实验验证 |
| GO-CC | nucleoplasm | IDA:HPA | 实验验证 |
| GO-CC | nucleus | IDA:UniProtKB | 实验验证 |

AKIRIN1是10个CRITICAL基因中唯一的纯核蛋白(HPA无任何胞质/膜信号)，且GO-CC含chromatin条目。Nuclear membrane附加定位与HPA Approved一致，提示AKIRIN1可能定位于内核膜或核孔复合物附近，这是许多核-质穿梭蛋白和核骨架蛋白的特征性定位模式。**修订评分: 7/10**。

#### 4.2 蛋白大小评估

192 aa / 21.9 kDa。极小的adaptor蛋白，为Akirin家族最小成员。作为分子桥接蛋白(bridge between proteins)，小尺寸可能是功能性特征——作为信号复合物的hub，小蛋白可以高效地在不同复合物间切换。但与标准核蛋白(如转录因子≥300aa)相比，功能域容量有限。**评分: 5/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 16 |
| PubMed symbol_only | 19 |
| 别名 | C1orf108 |
| 主要方向 | 骨骼肌发育、NF-kB信号、免疫 |

PubMed仅16篇(strict)，极度新颖。与AKIRIN2(广泛研究的蛋白酶体核转运因子)形成鲜明对比——AKIRIN1的功能领域完全不同且在文献中呈现"低关注度"。**评分: 10/10**。

**关键文献**:
1. Rao VV et al. (2019). "Role of Akirin1 in the regulation of skeletal muscle fiber-type switch." *J Cell Biochem*. PMID: 30746755
2. Sun W et al. (2019). "Akirin1 promotes myoblast differentiation by modulating multiple myoblast differentiation factors." *Biosci Rep*. PMID: 30777932
3. Coulibaly A et al. (2019). "AKIRIN1: A Potential New Reference Gene in Human Natural Killer Cells and Granulocytes in Sepsis." *Int J Mol Sci*. PMID: 31075840
4. Bosch PJ et al. (2020). "Akirin proteins in development and disease: critical roles and mechanisms of action." *Cell Mol Life Sci*. PMID: 32361777 -- 综述
5. Macqueen DJ et al. (2010). "Positioning the expanded akirin gene family of Atlantic salmon within the transcriptional networks of myogenesis." *Biochem Biophys Res Commun*. PMID: 20804733

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 68.1 |
| pLDDT > 90 (Very High) | 29.7% |
| pLDDT 70-90 (High) | 13.5% |
| pLDDT 50-70 (Medium) | 29.7% |
| pLDDT < 50 (Low) | 27.1% |
| 有序区域 (pLDDT>70) | 43.2% |
| 实验结构 (PDB) | 无 |

AlphaFold低质量预测(pLDDT 68.1)，仅43.2%有序。27.1%的pLDDT<50区域可能代表AKIRIN1作为adaptor蛋白的功能性无序区域，这类IDR(intrinsically disordered region)常用于介导多蛋白复合物中的灵活互作。小adaptor蛋白的高比例无序是功能特征而非结构缺陷——许多hub蛋白(如p53 N端、CREB binding protein)具有类似特征。但无PDB实验结构降低了结构可信度。**评分: 4/10**。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR024132 (Akirin family) |
| Pfam | 无 |

AKIRIN1属于Akirin家族，无已知Pfam功能域。作为分子adaptor，其功能通过蛋白-蛋白互作实现，不依赖酶活性或DNA结合。**与TE调控的潜在关联**: (1) GO-CC chromatin注释(IBA)暗示直接染色质结合; (2) 与RAN(核转运GTPase)和多个蛋白酶体亚基(PSMA5/PSMB3/PSMB9)的实验互作提示核蛋白输入和降解功能; (3) 通过PI3K通路调控actin细胞骨架重组，与核actin功能(染色质重塑、转录调控)有间接关联; (4) Akirin家族在果蝇中参与NF-kB先天免疫信号，该通路与内源性逆转录病毒防御交叉。**评分: 4/10**。

#### 4.6 PPI 网络

| Partner | Combined Score | Experimental | 功能 |
|---------|---------------|--------------|------|
| AKIRIN2 | 0.849 | 0.82 | 同家族互作 |
| PSMA5 | 0.686 | 0.685 | 20S蛋白酶体α亚基 |
| RAN | 0.636 | 0.612 | 核转运GTPase |
| DDX17 | 0.586 | 0.298 | RNA解旋酶 |
| KHDRBS1 | 0.583 | 0.292 | RNA结合/剪接因子 |
| PSMB3 | 0.551 | 0.55 | 20S蛋白酶体β亚基 |
| PSMB9 | 0.509 | 0.509 | 免疫蛋白酶体亚基 |
| PSMA2 | 0.465 | 0.466 | 20S蛋白酶体α亚基 |

**IntAct实验互作**: PSMB3(co-IP), RAN(co-IP), AKIRIN2(co-IP), PSMA5(co-IP), PSMB9(co-IP), PSMA2(co-IP), USP7(phage display, direct interaction), GOPC(Y2H array)

PPI网络高度集中于蛋白酶体(PSMA5/PSMB3/PSMB9/PSMA2)和核转运(RAN)，与Akirin家族保守的蛋白酶体调控功能一致。但值得注意的是，文献明确指出AKIRIN1(不同于AKIRIN2)不参与蛋白酶体核转运(PubMed:34711951)，暗示其蛋白酶体互作可能服务于不同功能——如在染色质上介导特定底物的泛素化降解。USP7(deubiquitinase)的直接互作进一步支持其泛素信号调控角色。**评分: 6/10** (PPI集中于蛋白酶体但实验证据扎实)。

### 5. Rescue Decision

**决策: RESCUED TO SCORED**

**核定位评分修正**: 从3/10 → 7/10。修正依据:
1. HPA Approved纯核定位(Nucleoplasm+Nuclear membrane)，无胞质信号
2. GO-CC含chromatin注释(IBA) -- 10个CRITICAL基因中独一无二
3. UniProt Nucleus IDA实验验证
4. GO-CC 4个核术语全部为实验级别(IDA)或保守推断(IBA)
5. PPI集中于蛋白酶体+核转运，功能指向核内蛋白降解

**修正后加权总分**: 121/180 (67.2/100)。

**AKIRIN1应进入scored蛋白列表**。尽管蛋白大小和结构质量偏弱，但其纯核定位(Approved HPA) + chromatin GO注释 + 极度新颖 + 实验PPI集中于核功能蛋白的组合使其成为TE调控研究的有趣候选——特别是如果其chromatin注释反映了在特定基因组区域(如TE位点)的富集。

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9L7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9L7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKIRIN1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000174574-AKIRIN1
- STRING: https://string-db.org/network/9606.ENSP00000366569
- IntAct: https://www.ebi.ac.uk/intact/interactors/id:Q9H9L7
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/AKIRIN1.json (2026-06-03)

HPA IF图像可在线获取(Approved, Nucleoplasm+Nuclear membrane)，未下载本地。PAE未生成本地。

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9L7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H9L7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024132; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174574-AKIRIN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKIRIN2 | Biogrid, Bioplex | true |
| GOPC | Intact | false |
| PSMA2 | Bioplex | false |
| PSMA6 | Opencell | false |
| PSMB7 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
