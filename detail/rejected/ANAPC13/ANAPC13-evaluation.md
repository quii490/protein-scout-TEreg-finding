---
type: protein-evaluation
gene: "ANAPC13"
date: 2026-06-04
tags: [protein-scout, confirmed-rejected, critical-false-rejection-recheck]
status: confirmed-rejected
previous_status: rejected
previous_rejection_reason: nuclear_score ≤ 3
recheck_result: "CONFIRMED REJECTED — HPA=Mitochondria+Cytosol(Approved); UniProt Nucleus仅ECO:0000305(curator inference,非实验); GO-CC无核术语; APC/C在核内执行功能但ANAPC13可能仅在胞质中组装; nuclear_score=3 borderline但接受原评分"
revised_nuclear_score: 3
---

## ANAPC13 核蛋白评估报告 -- FALSE REJECTION RE-EVALUATION (确认拒绝)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANAPC13 |
| 蛋白大小 | 74 aa / 8.5 kDa |
| UniProt ID | Q9BS18 |
| 蛋白全名 | Anaphase-promoting complex subunit 13 |
| HPA IF 主定位 | **Mitochondria, Cytosol** |
| HPA Reliability | Approved |
| 原评估状态 | REJECTED (nuclear_score=3) |
| 重新评估日期 | 2026-06-04 |
| CONFIRMED REJECTED | **CONFIRMED REJECTED** — 核定位证据严重不足 |

### 2. 评分总览（修订后，确认原评分）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **3/10** | ×4 | 12 | HPA=Mitochondria+Cytosol(Approved); UniProt Nucleus仅ECO:0000305; GO-CC仅anaphase-promoting complex |
| 蛋白大小 | 5/10 | ×1 | 5 | 74aa/8.5kDa，极端微型蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | pLDDT=73.6; 18个PDB EM结构(2.90-6.40A, 全长1-74覆盖) |
| 调控结构域 | 7/10 | ×2 | 14 | IPR008401/PF05839 (ANAPC13); APC/C E3泛素连接酶亚基 |
| PPI网络 | 8/10 | ×3 | 24 | STRING: 全部APC/C亚基0.993-0.999实验验证; IntAct: TAP纯化全实验 |
| **加权总分** | | | **135/180** | |
| **归一化总分 (÷1.8)** | | | **75.0/100** | |

### 3. False rejection recheck -- CRITICAL

**为何被列为CRITICAL进行重新评估:**

ANAPC13是10个CRITICAL基因中一个特殊案例: 其加权总分(135/180)实际上高于大多数rescued基因(如ALKBH2的133/180)。它拥有:
- 极度新颖(PubMed=11)
- 18个PDB实验结构(全部为EM，覆盖全长)
- APC/C E3泛素连接酶复合物全亚基的实验验证PPI网络(STRING scores 0.993-0.999)
- 仅有74aa的极端微型蛋白(结构生物学上极有趣)

ANAPC13被拒绝的唯一原因是核定位不足。APC/C复合物在细胞周期中执行核功能(介导有丝分裂调节因子的泛素化降解)，这引发了一个关键问题: ANAPC13作为核心亚基是否也在核内?

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet)**:
   - Nucleus: ECO:0000305 (curator inference — 非实验，非序列预测)
   - **单一定位，但证据等级极弱**
   - ECO:0000305 = "inferred by curator without traceable author statement" — 这是UniProt中最弱的证据等级之一

2. **GO-CC (harvest packet)**:
   - GO:0005680 anaphase-promoting complex: IDA:UniProtKB (实验)
   - **仅有一个GO-CC术语，且该术语描述的是蛋白质复合物而非亚细胞区室**
   - 没有nucleus, nucleoplasm, cytoplasm等任何亚细胞定位的GO-CC术语

3. **HPA Subcellular (harvest packet) -- 明确矛盾**:
   - Main location: **Mitochondria**, **Cytosol**
   - Reliability: **Approved (最高可信度)**
   - IF display images: 6张在线可用(blue_red_green)
   - **零核信号!**

4. **功能证据 -- 复合物功能 vs 亚基定位**:
   - APC/C复合物在有丝分裂中定位于核(spindle checkpoint, mitotic cyclin degradation)
   - 但ANAPC13仅74aa，可能在胞质中与APC/C复合物其他亚基组装，组装完成的复合物再进入核内
   - "anaphase-promoting complex"作为GO-CC术语描述的是复合物水平，而非单个亚基的亚细胞定位
   - ANAPC13可能从未独立于复合物进入细胞核

**为何这不是假阴性:**

ANAPC13面对一个核心矛盾:
- **复合物功能**: APC/C在有丝分裂中定位于核并降解核蛋白(cyclin B, securin等)
- **亚基定位数据**: HPA Approved显示Mitochondria+Cytosol，UniProt Nucleus仅ECO:0000305

这种矛盾在其他多亚基复合物中很常见: 支架亚基在胞质中组装复合物，功能性亚基(如共激活因子CDC20/CDH1)负责核定位。ANAPC13(又称APC13或SWM1)是最小的APC/C亚基，可能仅起结构支架作用——在胞质中稳定复合物，但不参与核靶向。

如果UniProt的Nucleus证据至少是ECO:0000269(实验)或GO-CC有nucleus/nucleoplasm(实验)，我会倾向于rescuing。但当前最佳实验数据(HPA Approved)显示Mitochondria+Cytosol，而仅有的核证据是curator inference(ECO:0000305)。

**修订后核定位评分: 3/10 (确认)。因APC/C复合物的核功能，将评分保持在3而非2，但HPA Approved Mitochondria+Cytosol + 极度弱UniProt证据不足以触发rescue。**

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | Mitochondria, Cytosol | **Approved** (最高) | IF实验，6张display images |
| UniProt | Nucleus | ECO:0000305 | **curator inference (非实验)** |
| GO-CC | anaphase-promoting complex (GO:0005680) | IDA:UniProtKB | 实验(但描述复合物而非区室) |

核定位证据完全依赖UniProt的一个弱备注(ECO:0000305)和APC/C复合物在有丝分裂中的核功能。HPA Approved实验数据的否定影响更大。Mitochondria信号可能是实验伪影(小蛋白(8.5kDa)的抗体可能与线粒体蛋白交叉反应)。**评分: 3/10**。

#### 4.2 蛋白大小评估

74 aa / 8.5 kDa。极端微型蛋白，是所有评估基因中最小的。可能代表了多亚基复合物中结构稳定的最小单元。太小而难以独立功能化——几乎肯定只能在APC/C复合物背景下执行功能。**评分: 5/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 11 |
| 主要方向 | APC/C复合物结构、SF3B1-K700E突变/Treg功能 |

极度新颖(11篇)。APC/C复合物整体研究深入(>5000篇)，但ANAPC13作为最小亚基几乎未被单独研究。**评分: 10/10**。

**关键文献**:
1. Shi Y et al. (2024). "SF3B1-K700E mutation controls immune responses by regulating Treg function via aberrant Anapc13 splicing." *Sci Adv*. PMID: 39303038
2. Wang D et al. (2017). "miRNA-mRNA regulation network of chronic pancreatitis." *Medicine*. PMID: 28538367
3. Abbas SZ et al. (2020). "Systems-level differential gene expression reveals new genetic variants of oral cancer." *Sci Rep*. PMID: 32887903
4. He K et al. (2025). "Identifying genes associated with Sorafenib resistance in hepatocellular carcinoma." *Discov Oncol*. PMID: 40835789
5. Jiang BJ et al. (2012). "ANAPC13 gene polymorphisms associated with body measurement traits in Bos taurus." *Genet Mol Res*. PMID: 22782628

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.6 |
| pLDDT > 90 (Very High) | 10.8% |
| pLDDT 70-90 (High) | 41.9% |
| pLDDT 50-70 (Medium) | 45.9% |
| pLDDT < 50 (Low) | 1.4% |
| 实验结构 (PDB) | 18个EM结构(2.90-6.40A, 全部覆盖全长1-74) |

**PDB条目**: 4UI9, 5G04, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW, 6Q6G, 6Q6H, 6TLJ, 6TM5, 6TNT, 8PKP, 8TAR, 8TAU, 9GAW, 9N9R, 9N9S

18个PDB结构全部为APC/C全复合物的冷冻电镜结构，ANAPC13仅作为其中一个小亚基被解析。最高分辨率2.90A(9GAW)。**评分: 10/10**。

#### 4.5 结构域分析

IPR008401/PF05839 (ANAPC13)。小亚基仅含一个结构域，在APC/C复合物中可能扮演结构稳定角色。调控潜力有限。**评分: 7/10** (因APC/C在细胞周期中的核心调控角色)。

#### 4.6 PPI 网络

| Partner | Combined Score | Experimental | 注释 |
|---------|---------------|--------------|------|
| CDC16 | 0.999 | 0.989 | APC/C亚基 |
| ANAPC5 | 0.999 | 0.987 | APC/C亚基 |
| CDC27 | 0.999 | 0.999 | APC/C亚基 |
| CDC23 | 0.999 | 0.991 | APC/C亚基 |
| ANAPC10 | 0.999 | 0.998 | APC/C亚基 |

所有APC/C亚基均实验验证(STRING experimental 0.929-0.999)。IntAct TAP实验全确认。10个CRITICAL基因中最强的PPI网络。但全部局限于APC/C自身。**评分: 8/10**。

### 5. 最终决定

**CONFIRMED REJECTED — 核定位证据严重不足，nuclear_score=3可接受**

ANAPC13是本次评估中最复杂的案例: 结构数据(18个PDB)、PPI网络(全APC/C实验验证)、新颖度(11篇)均为顶级，但核定位证据薄弱。HPA Approved的实验数据显示Mitochondria+Cytosol，而非Nucleus/Nucleoplasm。UniProt的唯一核证据是ECO:0000305(curator inference)。

**为什么nuclear_score=3不是假阴性**:
- HPA Approved否定核定位
- UniProt核证据是最弱等级
- GO-CC无任何亚细胞区室术语
- 蛋白太小(74aa)难以独立核定位——依赖整个APC/C复合物的运输

**与其他类似案例的比较**: 与ALKBH2(3个核区室均为IDA，18个PDB支持核功能)的rescued形成鲜明对比。ANAPC13虽然有18个PDB结构，但这些结构展示的是APC/C全复合物(非ANAPC13单独)，且APC/C在有丝分裂中的核定位是由其他亚基(如CDC20/CDH1/RAP1)介导的。

**边界提示**: 如果未来的实验数据(如细胞周期同步化后的IF、核质分离Western blot)显示ANAPC13在M期确实位于核内，该基因应重新评估。但当前数据不支持rescue。

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BS18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BS18
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANAPC13%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000129055-ANAPC13
- STRING: https://string-db.org/network/9606.ENSP00000361538
- IntAct: https://www.ebi.ac.uk/intact/interactors/id:Q9BS18
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/ANAPC13.json (2026-06-03)

HPA IF图像在线可用(6张blue_red_green, Mitochondria+Cytosol信号)，未下载本地。PAE未生成本地。
