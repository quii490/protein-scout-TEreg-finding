---
type: protein-evaluation
gene: "AFMID"
date: 2026-06-04
tags: [protein-scout, confirmed-rejected, critical-false-rejection-recheck]
status: confirmed-rejected
previous_status: rejected
previous_rejection_reason: nuclear_score ≤ 3 (HPA=Mitochondria)
recheck_result: "CONFIRMED REJECTED — HPA确定为Mitochondria(Approved); UniProt Nucleus仅ECO:0000255(序列预测); GO-CC Nucleus仅IEA(电子注释); 无任何实验核定位证据; 原始nuclear_score=2准确"
revised_nuclear_score: 2
---

## AFMID 核蛋白评估报告 -- FALSE REJECTION RE-EVALUATION (确认拒绝)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AFMID / 无已知别名(原Sheet4名Kynurenine formamidase) |
| 蛋白大小 | 303 aa / 34.0 kDa |
| UniProt ID | Q63HM1 |
| 蛋白全名 | Kynurenine formamidase (Arylformamidase) |
| HPA IF 主定位 | **Mitochondria** |
| HPA Reliability | Approved |
| 原评估状态 | REJECTED (nuclear_score=2, HPA=Mitochondria) |
| 重新评估日期 | 2026-06-04 |
| CONFIRMED REJECTED | **CONFIRMED REJECTED** — 非核蛋白 |

### 2. 评分总览（修订后，确认原评分）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **2/10** | ×4 | 8 | HPA=Mitochondria(Approved); UniProt Nucleus仅ECO:0000255序列预测; GO-CC Nucleus仅IEA电子注释 |
| 蛋白大小 | 9/10 | ×1 | 9 | 303aa/34.0kDa，实验理想大小 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT=94.0, 90.8%>90; 无PDB实验结构 |
| 调控结构域 | 2/10 | ×2 | 4 | Kynurenine formamidase -- 代谢酶, 无染色质/TE调控关联 |
| PPI网络 | 1/10 | ×3 | 3 | STRING不可用(HTTP 502); IntAct仅高通量Y2H+ChIP(非PPI) |
| **加权总分** | | | **95/180** | |
| **归一化总分 (÷1.8)** | | | **52.8/100** | |

### 3. False rejection recheck -- CRITICAL

**为何被列为CRITICAL进行重新评估:**

AFMID在原始Sheet4中被错误记录为HPA定位"Nucleoli|Nucleoli fibrillar center|Nucleoplasm"并分配nuclear_score=6，但在harvest packet(2026-06-03)中HPA明确显示为Mitochondria(Approved)。两个数据源之间存在根本性冲突。本次re-evaluation的目的是确认哪个数据源反映真实生物学情况，并决定是否推翻原rejection。

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet)**:
   - Cytoplasm, cytosol: ECO:0000255 (sequence analysis prediction)
   - Nucleus: ECO:0000255 (sequence analysis prediction)
   - **两个定位证据代码均为ECO:0000255 — 序列分析预测，非实验证据**
   - ECO:0000255在UniProt证据等级中是最低层级的(非实验)

2. **GO-CC (harvest packet)**:
   - GO:0005737 cytoplasm: IBA:GO_Central (生物学推断)
   - GO:0005829 cytosol: IEA:UniProtKB-SubCell (电子自动注释，非人工审核)
   - GO:0005634 nucleus: IEA:UniProtKB-SubCell (电子自动注释，非人工审核)
   - **所有GO条目均非实验证据(IDAs absent)**

3. **HPA Subcellular (harvest packet) -- 决定性证据**:
   - Main location: **Mitochondria**
   - Additional: 无
   - Reliability: **Approved (最高可信度!)**
   - IF display images: **6张在线可用** (blue_red_green triple channel)
   - HPA Approved Mitochondria与所有核定位推断形成直接矛盾

4. **功能证据**:
   - Kynurenine formamidase — 催化tryptophan降解通路第二步: N-formyl-L-kynurenine → L-kynurenine
   - 这是一种典型代谢酶功能，在胞质(cytosol)中执行
   - Tryptophan降解通路与免疫调节、神经递质合成相关，与染色质/TE无已知功能关联
   - 功能本身预设胞质/线粒体定位，不支持核定位

5. **结构证据**:
   - AlphaFold pLDDT=94.0 (极高质量预测)
   - alpha/beta hydrolase折叠 — 典型代谢酶折叠
   - 无PDB实验结构

**为何这不是假阴性:**

AFMID的"核定位"证据完全来自非实验来源:
- UniProt Nucleus: ECO:0000255 = 序列分析预测(基于序列与已知核蛋白的相似性)
- GO-CC Nucleus: IEA = 电子注释(由UniProtKB-SubCell pipeline自动推断)

而决定性的**实验证据指向线粒体**:
- HPA Approved Mitochondria (最高可信度，6张IF display images)
- 无任何HPA核信号

实验证据(HPA)的权重 >> 计算预测(UniProt ECO:0000255 / GO IEA)。

**关于Sheet4数据差异的说明:**
原Sheet4记录AFMID的HPA为"Nucleoli|Nucleoli fibrillar center|Nucleoplasm"并设nuclear_score=6，这与harvest packet的Mitochondria数据完全矛盾。差异可能源于:
(1) HPA数据库版本更新导致定位变更 (最常见原因)
(2) Sheet4使用了不同的基因symbol或Ensembl ID匹配
(3) 数据抓取过程中的人为错误
(4) 基因symbol混淆(AFMID vs 其他基因)
鉴于harvest packet使用2026-06-03的最新HPA API(含直接subcellular URL验证: ENSG00000183077-AFMID)，应以harvest packet为准。

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | **Mitochondria** (main) | **Approved (最高)** | IF实验，6张display images |
| UniProt | Cytoplasm, cytosol | ECO:0000255 | **序列分析预测** |
| UniProt | Nucleus | ECO:0000255 | **序列分析预测** |
| GO-CC | cytoplasm | IBA:GO_Central | 生物学推断 |
| GO-CC | cytosol | IEA:UniProtKB-SubCell | **电子自动注释** |
| GO-CC | nucleus | IEA:UniProtKB-SubCell | **电子自动注释** |

AFMID的核定位"证据"完全由两层自动推断组成: UniProt ECO:0000255(序列分析预测)和GO IEA(电子注释)。HPA Approved的IF实验数据(实验验证的黄金标准)明确指向Mitochondria。三个数据源的层级比较: HPA Approved(实验) >> UniProt ECO:0000255(预测) ≈ GO IEA(电子)。

**核定位特异性评分: 2/10 (确认)。该评分已考虑到UniProt和GO的预测性注释，但因为无实验证据且HPA明确定位为线粒体，不能给更高分数。**

#### 4.2 蛋白大小评估

303 aa / 34.0 kDa。接近生化实验的理想大小范围。蛋白足够大以容纳稳定折叠域但不过大而难以表达。AlphaFold的结构置信度(94.0)进一步验证了其折叠稳定性。**评分: 9/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 13 |
| PubMed symbol_only | 22 |
| 别名 | 无 |
| 主要方向 | 色氨酸/犬尿氨酸代谢通路、葡萄糖耐受性 |

极度新颖(13篇)，但所有文献均集中于tryptophan代谢通路，与核功能/染色质/TE调控无关联。**评分: 10/10**。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 94.0 |
| pLDDT > 90 (Very High) | 90.8% |
| pLDDT < 50 (Low) | 3.6% |
| 有序区域 (pLDDT>70) | 95.8% |
| 实验结构 (PDB) | 无 |

结构预测质量极高(94.0)，但无实验结构验证。alpha/beta hydrolase折叠的N端和C端可能存在少量柔性loop(对应3.6%的低置信区域)。**评分: 7/10**。

#### 4.5 结构域分析

Kynurenine formamidase (IPR050300) — 纯代谢酶。催化tryptophan→kynurenine通路。无任何染色质/转录/TE调控相关结构域。**评分: 2/10**。

#### 4.6 PPI 网络

IntAct仅6个互作(DDIT4L, MED18, MEI4, Ahr[ChIP], Esr1[ChIP], STC2[co-IP])，其中Ahr/Esr1为ChIP(转录因子对AFMID启动子的结合，非蛋白互作)。STRING HTTP 502不可用。无有意义的功能PPI网络。**评分: 1/10**。

### 5. 最终决定

**CONFIRMED REJECTED — 非核蛋白，nuclear_score=2 准确**

AFMID的生物学现实: 线粒体定位的代谢酶，参与tryptophan降解。尽管新颖度高(PubMed=13)且AlphaFold结构质量极佳(94.0)，但**缺乏实验核定位证据**是致命的。HPA Approved Mitochondria与UniProt/GO的非实验预测形成鲜明对比——在蛋白质亚细胞定位评估中，实验证据的权重大于计算预测。

**拒绝的三个核心原因**:
1. HPA Approved Mitochondria (黄金标准实验证据) 否定核定位
2. UniProt "Nucleus"为序列分析预测(ECO:0000255)，非实验证据
3. 功能为胞质代谢酶(tryptophan降解)，无核/染色质功能关联

**不建议再次重新评估**。除非新的实验数据(如细胞周期依赖性核转位、组织特异性核定位)推翻了HPA Mitochondria结论。

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q63HM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q63HM1
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q63HM1/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AFMID[Title/Abstract]
- HPA: https://www.proteinatlas.org/ENSG00000183077-AFMID
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/AFMID.json (2026-06-03)

HPA IF原图可在线获取(6张blue_red_green, Mitochondria信号)，未下载本地。PAE未生成本地。
